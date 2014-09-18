# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
    _name = 'co.multimedia'
    _description = 'CO Multimedia'
    _rec_name = 'title'
<<<<<<< HEAD
    _order = 'release_date desc'
    
    def _compute_stock(self, cr, uid, ids, field_name, arg,context):
		stock_obj = self.pool.get('co.lineas.stock')
		
		if isinstance(ids, (int, long)):
			ids = [ids]
			
		res = {}
		for i in ids:
			lineas_ids = stock_obj.search(cr, uid, [
				('multimedia_id', '=', i), ])
			lineas_brw = stock_obj.browse(cr, uid, lineas_ids)
			res[i] = sum([l.quantity for l in lineas_brw])
		return res
    
    _columns = {
        'title': fields.char('Título', required=True),
        'release_date': fields.date('Fecha de publicación'),
        'code': fields.char('Código'),
        'categoria_id': fields.many2one('co.categoria', 'Categoría'),
=======
    _order = 'release_date'

    _columns = {
        'title': fields.char('Titulo', required=True),
        'release_date': fields.date('Fecha de publicación'),
        'code': fields.char('Código'),
        'categoria_id': fields.many2one('co.categoria', 'Categoria'),
>>>>>>> 49e77823fa409c00b7c13482df75d9f23f5fed1c
        'medio_ids': fields.many2many(
            'co.tipo.medio',
            'co_multimedia_medio_rel',
            'multimedia_id',
<<<<<<< HEAD
            'medio_id'),            
		'stock': fields.function(_compute_stock, type='integer'),
      
    }
    
multimedia()
=======
            'medio_id',),
    }


multimedia()
>>>>>>> 49e77823fa409c00b7c13482df75d9f23f5fed1c
