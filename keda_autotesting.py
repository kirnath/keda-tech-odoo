import unittest
import requests
import json

class TestMaterialAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://localhost:8069/materials'
        cls.session = requests.Session()

    def test_get_all_materials(self):
        print("Testing: Get All Materials")
        response = self.session.get(self.base_url)
        materials = json.loads(response.text)
        self.assertGreaterEqual(len(materials), 1, "Materials list should contain at least one entry.")

    def test_create_material_valid_data(self):
        print("Testing: Create Material => VALID DATA")
        create_url = f'{self.base_url}/create'
        data = {
            'name': 'test create',
            'code': 'TCRT-001',
            'type': 'fabric',
            'buy_price': 10000,
            'related_supplier': 1
        }
        response = self.session.post(create_url, data=data)
        result = response.json()
        self.assertTrue(result.get('success'), "Material creation with valid data should be successful.")
        print(response.text)

    def test_create_material_invalid_data(self):
        print("Testing: Create Material => INVALID DATA")
        create_url = f'{self.base_url}/create'
        data = {
            'name': 'test create',
            'buy_price': 10000,
            'related_supplier': 1
        }
        response = self.session.post(create_url, data=data)
        result = response.json()
        self.assertFalse(result.get('success'), "Material creation with invalid data should fail.")
        print(response.text)

    def test_update_material_valid_data(self):
        print("Testing: Update Material => VALID DATA")
        update_url = f'{self.base_url}/update'
        data = {
            'id': 10,  # Adjust with a valid ID
            'name': 'test update',
            'code': 'UUPDT-001',
            'type': 'fabric',
            'buy_price': 10000,
            'related_supplier': 1
        }
        response = self.session.post(update_url, data=data)
        result = response.json()
        self.assertTrue(result.get('success'), "Updating material with valid data should be successful.")
        print(response.text)

    def test_update_material_invalid_data(self):
        print("Testing: Update Material => INVALID DATA")
        update_url = f'{self.base_url}/update'
        data = {
            'id': 0,  # Adjust with invalid ID
            'name': 'test update',
            'buy_price': 10000,
            'related_supplier': 1
        }
        response = self.session.post(update_url, data=data)
        result = response.json()
        self.assertFalse(result.get('success'), "Updating material with invalid data should fail.")
        print(response.text)

    def test_delete_material_valid_id(self):
        print("Testing: Delete Material Data => VALID ID")
        delete_url = f'{self.base_url}/delete'
        data = {'id': 12}  # Adjust with a valid ID
        response = self.session.delete(delete_url, data=data)
        result = response.json()
        self.assertTrue(result.get('success'), "Deleting material with a valid ID should be successful.")
        print(response.text)

    def test_delete_material_invalid_id(self):
        print("Testing: Delete Material Data => INVALID ID")
        delete_url = f'{self.base_url}/delete'
        data = {'id': 999}  # Invalid ID
        response = self.session.delete(delete_url, data=data)
        result = response.json()
        self.assertFalse(result.get('success'), "Deleting material with an invalid ID should fail.")
        print(response.text)

    def test_delete_material_undefined_id(self):
        print("Testing: Delete Material Data => UNDEFINED ID")
        delete_url = f'{self.base_url}/delete'
        data = {'id': ''}  # Undefined ID
        response = self.session.delete(delete_url, data=data)
        result = response.json()
        self.assertFalse(result.get('success'), "Deleting material with an undefined ID should fail.")
        print(response.text)

if __name__ == '__main__':
    unittest.main()
