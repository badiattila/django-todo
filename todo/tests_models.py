from django.test import TestCase
from .models import Item 

# Create your tests here.
class TestModel(TestCase):
    def test_done_defaults_to_false(self):
        item = Item(name="Create a test")
        item.save()
        self.assertEqual(item.name, "Create a test")
        self.assertFalse(item.done)
        
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="Create a test", done=True)
        item.save()
        self.assertEqual(item.name, "Create a test")
        self.assertTrue(item.done)
        
    def test_item_as_a_string(self):
        item = Item(name="Create a test")
        item.save()
        self.assertEqual(str(item), "Create a test")
        