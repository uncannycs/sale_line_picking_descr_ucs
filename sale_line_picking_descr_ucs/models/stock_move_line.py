# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.depends('sale_line_id')
    def _compute_description_picking(self):
        super()._compute_description_picking()
        for move in self:
            if move.sale_line_id and move.sale_line_id.name and not move.description_picking_manual:
                name = move.sale_line_id.name
                # Strip product name/reference prefix to avoid duplication in the form view
                # (the form already shows product_id separately above the description)
                for prefix in [move.product_id.display_name, move.product_id.name]:
                    if prefix and name.startswith(prefix):
                        name = name[len(prefix):].lstrip('\n').strip()
                        break
                move.description_picking = name



class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sh_so_line_desc_sml = fields.Text(
        related="move_id.description_picking", string="Description")

    def _get_aggregated_product_quantities(self, **kwargs):
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for line_key, values in aggregated_move_lines.items():
            values['sh_so_line_desc_sml'] = values.get('description', '')
        return aggregated_move_lines

