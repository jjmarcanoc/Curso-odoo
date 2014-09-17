# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class solicitud(osv.osv):
    _name = 'co.solicitud'
    _description = 'CO Solicitud'
    _rec_name = 'code'
    
    _columns = {
        'code': fields.char('Código'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
        'multimedia_id': fields.many2one('co.multimedia', 'Multimedia'),
        'medio_id': fields.many2one('co.tipo.medio', 'Tipo de medio'),
        'tienda_id': fields.many2one('co.tienda', 'Origen'),
        'requested_date': fields.date('Fecha solicitada'),
        'qty_days': fields.integer('Duración (en días)'),
    }
    
solicitud()
