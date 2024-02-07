from odoo import models, fields

class PokemonList(models.Model):
    _name = 'pokemon.list'
    _description = 'Pokemon'

    name = fields.Char(string='Pokemon ID', help='ID of your pokemon', readonly=True)
    pokemon_name = fields.Char(string='Pokemon Name', help='Name of the pokemon')
    stats_info = fields.Text(string='Pokemon Stats', help='Stats of the pokemon')
    partner_id = fields.One2many('res.partner', 'pokemon_id', string='Partner ID', help='Partner associated with pokemon')
    partner_name = fields.Char(related='partner_id.name', string='Partner', help='Name')