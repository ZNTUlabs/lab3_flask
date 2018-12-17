import unittest
import requests

class TestApiMethods(unittest.TestCase):
	def getServerUrl(self):
		return "http://192.168.43.159"

	def test_pin_off_all(self):
		r = requests.get(self.getServerUrl() + '/pin/off/all')
		self.assertEqual(r.status_code, 200)

# //[7,8,18,16,15,13,12,11]
	def test_pin_on_1(self):
		r = requests.get(self.getServerUrl() + '/pin/on/7')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_2(self):
		r = requests.get(self.getServerUrl() + '/pin/on/8')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_3(self):
		r = requests.get(self.getServerUrl() + '/pin/on/18')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_4(self):
		r = requests.get(self.getServerUrl() + '/pin/on/16')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_5(self):
		r = requests.get(self.getServerUrl() + '/pin/on/15')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_6(self):
		r = requests.get(self.getServerUrl() + '/pin/on/13')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_7(self):
		r = requests.get(self.getServerUrl() + '/pin/on/12')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_8(self):
		r = requests.get(self.getServerUrl() + '/pin/on/11')
		self.assertEqual(r.status_code, 200)

#  OFF ****************************************************

	def test_pin_off_1(self):
		r = requests.get(self.getServerUrl() + '/pin/off/7')
		self.assertEqual(r.status_code, 200)

	def test_pin_off_2(self):
		r = requests.get(self.getServerUrl() + '/pin/off/8')
		self.assertEqual(r.status_code, 200)

	def test_pin_off_3(self):
		r = requests.get(self.getServerUrl() + '/pin/off/18')
		self.assertEqual(r.status_code, 200)

	def test_pin_off_4(self):
		r = requests.get(self.getServerUrl() + '/pin/off/16')
		self.assertEqual(r.status_code, 200)

	def test_pin_off_5(self):
		r = requests.get(self.getServerUrl() + '/pin/off/15')
		self.assertEqual(r.status_code, 200)

	def test_pin_off_6(self):
		r = requests.get(self.getServerUrl() + '/pin/off/13')
		self.assertEqual(r.status_code, 200)

	def test_pin_off_7(self):
		r = requests.get(self.getServerUrl() + '/pin/ooffn/12')
		self.assertEqual(r.status_code, 200)

	def test_pin_off_8(self):
		r = requests.get(self.getServerUrl() + '/pin/off/11')
		self.assertEqual(r.status_code, 200)

	def test_pin_on_all(self):
		r = requests.get(self.getServerUrl() + '/pin/on/all')
		self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()