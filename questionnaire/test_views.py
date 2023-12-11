from django.test import TestCase

# Create your tests here.

class TestDjango(TestCase):

    def test_workability(self):
        self.assertEqual(1, 1)

    def test_workability2(self):
        self.assertEqual(1, 3)
    
    def test_workability3(self):
        self.assertEqual(1, )
    
    def test_workability4(self):
        self.assertEqual(1, 4)
