# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class categoria(osv.osv):
    _name = 'co.categoria'
    _descripcion = 'CO Categoria'

    _columns = {
        "active": fields.boolean("active"),
        'name': fields.char('Nombre'),
        'code': fields.char('Codigo'),
        'description': fields.text('Descripción'),
        'parent_id': fields.many2one('co.categoria', 'Padre'),
        'child_ids': fields.one2many(
            'co.categoria',
            'parent_id',
            'Sub-categoria'),
    }

categoria()