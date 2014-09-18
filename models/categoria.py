# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class categoria(osv.osv):
    _name = 'co.categoria'
<<<<<<< HEAD
    _description = 'CO Categoria'
    
    _columns = {
        'name': fields.char('Nombre'),
        'description': fields.text('Descripción'),
        'parent_id': fields.many2one('co.categoria', 'Padre'),
        'child_ids': fields.one2many(
            'co.categoria', 
            'parent_id', 
            'Sub-categorías'), 
    }
    
categoria()
=======
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
>>>>>>> 49e77823fa409c00b7c13482df75d9f23f5fed1c
