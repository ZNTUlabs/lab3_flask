import unittest
import requests

class TestApiMethods(unittest.TestCase):
	def getServerUrl(self):
		return "http://192.168.43.159"

	def test_pin_off_all(self):
		r = requests.get(self.getServerUrl() + '/pin/off/all')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_all(self):
		r = requests.get(self.getServerUrl() + '/pin/on/all')
		self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()