# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class lineas_stock(osv.osv):
    _name = 'co.lineas.stock'
    _descripcion = 'CO Lineas Stock'

    _columns = {
        'multimedia_id': fields.many2one('co.multimedia', 'Multimedia'),
        'tipo_medio_id': fields.many2one('co.tipo.medio', 'Tipo de medio'),
        'tienda_id': fields.many2one('co.tienda', 'Tienda'),
        'quantity': fields.integer('Cantidad'),
    }

lineas_stock()


class tienda(osv.osv):
    _inherit = 'co.tienda'

    _columns = {
        'stock_ids': fields.one2many('co.lineas.stock', 'tienda_id', 'Stock'),
    }

tienda()
