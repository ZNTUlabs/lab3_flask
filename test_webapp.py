import unittest
import requests

class TestApiMethods(unittest.TestCase):

	def test_pin_off_all(self):
		r = requests.get('http://192.168.1.6/pin/off/all')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_all(self):
		r = requests.get('http://192.168.1.6/pin/on/all')
		self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()