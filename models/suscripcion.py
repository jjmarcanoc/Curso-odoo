# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime

TIPOS = [
    ('oro', 'Plan ORO'),
    ('plata', 'Plan PLATA'),
<<<<<<< HEAD
    ('bronce', 'Plan BRONCE'),
]

=======
    ('bronce', 'Plan BRONCE'),]
>>>>>>> 49e77823fa409c00b7c13482df75d9f23f5fed1c

class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _description = 'CO Suscripcion'
<<<<<<< HEAD
    _rec_name = 'code'
    
    _columns = {
        'code': fields.char('Código',
        help="Codigo se genera de forma automatica"),
        'type': fields.selection(TIPOS, 'Tipo de suscripción', required=True),
        'date_start': fields.date('Inicio suscripción', required= True),
        'date_end': fields.date('Fin suscripción', required=True),
        'active': fields.boolean('Activo'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
    }
    
    _defaults = {
        'active': True,
        'date_start': datetime.now().strftime('%Y-%m-%d'),
    }
    
    def _check_dates(self, cr, uid, ids, context=None):
		if isinstance(ids, (int, long)):
			ids = [ids]
		for s in self.browse(cr, uid, ids, context=context):
			if s.date_end <= s.date_start:
				return False
		return True

    _constraints = [
		(_check_dates, 'Fecha de inicio debe ser menor a la fecha final',
		['date_start', 'date_end'])
    ]
        
    def create(self, cr, uid, values, context=None):
        if context is None:
            context = {}
            
        values.update({
            'code': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
            
        return super(suscripcion, self).create(cr, uid, values, context=context)
    
suscripcion()






    
=======

    _columns = {
        'code': fields.char('Código'),
        'type': fields.selection(TIPOS, 'Tipo de suscripción'),
        'date_start': fields.date('Inicio suscripción'),
        'date_end': fields.date('Fin suscripción'),
        'active': fields.boolean('Activo'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
    }

    _default = {
        'active': True,
        'date_start': datetime.now().strftime('%Y-%m-&d'),
    }

    def create(self, cr, uid, ids, values, context=None):
        if context is None:
            context = {}

        values.update({
            'code': self.pool.get('ir.secuence').get(cr,uid, 'seq.suscripcion')})

        return super(suscripcion, self).create(cr, uid, values, context=context)

suscripcion()
>>>>>>> 49e77823fa409c00b7c13482df75d9f23f5fed1c
