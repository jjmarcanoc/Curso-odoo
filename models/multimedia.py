# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
    _name = 'co.multimedia'
    _description = 'CO Multimedia'

    _columns = {
        'title': fields.char('Titulo'),
        'release date': fields.date('Fecha de publicación'),
        'code': fields.char('Código'),
        'categoria_id': fields.many2one('co.categoria', 'Categoria'),
        'medio_ids': fields.many2many(
            'co.tipo.medio',
            'co_multimedia_medio_rel',
            'multimedia_id',
            'medio_id',),
    }


multimedia()