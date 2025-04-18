import unittest
import requests
from unittest.mock import patch

class TestAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}

        response = requests.get('https://rickandmortyapi.com/api/character')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})
        mock_get.assert_called_once_with('https://rickandmortyapi.com/api/character')

    @patch('requests.get')
    def test_get_data_error(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        response = requests.get('https://rickandmortyapi.com/api/character')

        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()