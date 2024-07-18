import unittest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rubles


class TestConvertToRubles(unittest.TestCase):
    @patch('src.utils.requests.get')
    def test_convert_to_rubles_success(self, mock_get):
        result = {'result': 123.45}
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = result
        mock_get.return_value = mock_response

        amount = 100
        currency_code = 'USD'
        converted_amount = convert_to_rubles(amount, currency_code)

        self.assertEqual(converted_amount, result['result'])

    @patch('src.utils.requests.get')
    def test_convert_to_rubles_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        amount = 100
        currency_code = 'EUR'
        converted_amount = convert_to_rubles(amount, currency_code)

        self.assertIsNone(converted_amount)


if __name__ == '__main__':
    unittest.main()
