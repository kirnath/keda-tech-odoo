# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class MaterialCustom(http.Controller):
    
    @http.route(['/materials'], type="http", auth="public", website="True")
    def get_material_data(self, **kwargs):
        sort = kwargs.get('sort', None)
        domain = []
        if sort:
            domain.append(('type', '=', sort))
        materials = request.env['material.custom'].sudo().search(domain)
        result = []
        for material in materials:
            result.append({
                'id': material.id,
                'name': material.name,
                'code': material.code,
                'type': material.type,
                'buy_price': material.buy_price,
                'related_supplier_id': material.related_supplier.id
            })

        result = {
            'items': result,
            'total_data': len(result)
        }
        return json.dumps(result, default=str)
    
    @http.route(['/materials/create'], type="http", auth="none", methods=['POST'], csrf=False)
    def create_material_data(self, **post):
        required_fields = [ 'name', 'code', 'type', 'buy_price', 'related_supplier']
        missing_fields = [field for field in required_fields if not post.get(field)]

        if missing_fields:
            return json.dumps({'success': False, 'msg': 'Missing required fields: %s' % ', '.join(missing_fields)})  
        material = request.env['material.custom'].create({
            'name': post.get('name'),
            'code': post.get('code'),
            'type': post.get('type'),
            'buy_price': post.get('buy_price'),
            'related_supplier': post.get('related_supplier')
        })
        return json.dumps({'success': True, 'id': material.id}, default=str)
    
    @http.route('/materials/update', type='http', auth='none', methods=['POST'], csrf=False)
    def create_data(self, **post):
        required_fields = ['id', 'name', 'code', 'type', 'buy_price', 'related_supplier']
        missing_fields = [field for field in required_fields if not post.get(field)]

        if missing_fields:
            return json.dumps({'success': False, 'msg': 'Missing required fields: %s' % ', '.join(missing_fields)})
        try:
            material_id = post.get('id')
            material = request.env['material.custom'].sudo().search([('id', '=', material_id)])
            if not material.exists():
                print(material)
                return json.dumps({'error': 'Material not found'})
            material.write({
                'name': post.get('name'),
                'code': post.get('code'),
                'type': post.get('type'),
                'buy_price': post.get('buy_price'),
                'related_supplier': post.get('related_supplier')
            })
            return json.dumps({'success': True, 'id': material_id})
        except:
            return json.dumps({'error': 'Invalid input'})
        
    
    @http.route(['/materials/delete'], type="http", auth="none", methods=['DELETE'], csrf=False)
    def update_material_data(self, **kwargs):
        material_id = kwargs.get('id')

        if not material_id:
            return json.dumps({'success':False, 'msg': 'Invalid input'}, default=str)

        material = request.env['material.custom'].sudo().search([('id', '=', material_id)])
        if not material.exists():
            return json.dumps({'success':False, 'msg': 'Material not found'}, default=str)

        material.unlink()
        return json.dumps({'success': True, 'id': material_id}, default=str)
    
