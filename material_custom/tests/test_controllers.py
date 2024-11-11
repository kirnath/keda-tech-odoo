import unittest
from unittest.mock import patch, MagicMock
from odoo.http import request

from odoo.addons.material_custom.controllers import controllers


class TestMaterialCustom(unittest.TestCase):

    @patch('odoo.http.request')
    def test_get_material_data(self, mock_request):
        # Mock the environment and search method
        mock_env = MagicMock()
        mock_request.env = mock_env
        mock_material_model = mock_env['material.custom']
        mock_material_model.search.return_value = [
            MagicMock(id=1, name='Material 1', code='M001', type='fabric', buy_price=150, related_supplier=MagicMock(name='Supplier 1')),
            MagicMock(id=2, name='Material 2', code='M002', type='jeans', buy_price=200, related_supplier=MagicMock(name='Supplier 2'))
        ]

        # Instantiate the controller and call the method
        controller = controllers()
        response = controller.get_material_data(sort='fabric')

        # Parse the JSON response
        response_data = json.loads(response)

        # Assertions
        self.assertEqual(response_data['total_data'], 2)
        self.assertEqual(response_data['items'][0]['name'], 'Material 1')
        self.assertEqual(response_data['items'][1]['name'], 'Material 2')
        self.assertEqual(response_data['items'][0]['related_supplier'], 'Supplier 1')
        self.assertEqual(response_data['items'][1]['related_supplier'], 'Supplier 2')

if __name__ == '__main__':
    unittest.main()
    print("All tests passed!")