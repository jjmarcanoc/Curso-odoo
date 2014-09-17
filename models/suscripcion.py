# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime

TIPOS = [
    ('oro', 'Plan ORO'),
    ('plata', 'Plan PLATA'),
    ('bronce', 'Plan BRONCE'),
]


class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _description = 'CO Suscripcion'
    
    _columns = {
        'code': fields.char('Código'),
        'type': fields.selection(TIPOS, 'Tipo de suscripción'),
        'date_start': fields.date('Inicio suscripción'),
        'date_end': fields.date('Fin suscripción'),
        'active': fields.boolean('Activo'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
    }
    
    _defaults = {
        'active': True,
        'date_start': datetime.now().strftime('%Y-%m-%d'),
    }
    
    def create(self, cr, uid, values, context=None):
        if context is None:
            context = {}
            
        values.update({
            'code': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
            
        return super(suscripcion, self).create(cr, uid, values, context=context)
    
suscripcion()






    
