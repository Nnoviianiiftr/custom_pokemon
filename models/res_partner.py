from odoo import models, fields, api
import requests
import random

class ResPartner(models.Model):
    _inherit = 'res.partner'

    pokemon_id = fields.Many2one('pokemon.list', string='Pokemon ID', help='ID of your pokemon', readonly=True, ondelete='set null')
    pokemon = fields.Char(related='pokemon_id.name', string='Pokemon Name', help='Name of your pokemon')
    pokemon_name = fields.Char(related='pokemon_id.pokemon_name', string='Pokemon Name', help='Name of your pokemon')
    stats_info = fields.Text(related='pokemon_id.stats_info', string='Pokemon Stats', help='Stats of your pokemon')

    def write(self, vals):
        if 'is_company' in vals and not vals['is_company']:
            if self.pokemon_id:
                old_pokemon = self.pokemon_id
                self.pokemon_id = None
                old_pokemon.unlink()
        return super(ResPartner, self).write(vals)

    def generate_random_number(self):
        return random.randint(1, 100)
    
    def get_unique_random_number(self):
        used_numbers = self.env['res.partner'].search([('pokemon_id', '!=', False)]).mapped('pokemon_id.id')
        random_number = random.randint(1, 100)
        while random_number in used_numbers:
            random_number = random.randint(1, 100)
        return random_number

    def get_pokemon(self):
        random_number = self.get_unique_random_number()
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_number}/')
        data = response.json()

        pokemon_name = data['name']
        pokemon_id = data['id']
        stats_data = data['stats']
        stats_info = '\n'.join([f"{index['stat']['name']}: {index['base_stat']}" for index in stats_data])

        if self.pokemon_id:
            old_pokemon_id = self.pokemon_id.id
            partners = self.env['res.partner'].search([('pokemon_id', '=', old_pokemon_id)])
            for partner in partners:
                partner.pokemon_id = None
            self.env['pokemon.list'].browse(old_pokemon_id).unlink()

        pokemon = self.env['pokemon.list'].create({
            'name': str(pokemon_id),
            'pokemon_name': pokemon_name,
            'stats_info': stats_info,
        })
        self.pokemon_id = pokemon.id
