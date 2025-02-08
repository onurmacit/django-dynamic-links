from django.test import TestCase
from django.core.exceptions import ValidationError
from ..factories import ItemFactory  

class ItemModelTest(TestCase):
    def test_item_creation(self):
        """
        Test that an Item instance can be created using the factory.
        """
        item = ItemFactory() 
        self.assertIsNotNone(item.id)  
        self.assertIsNotNone(item.title) 
        self.assertIsNotNone(item.description)  

    def test_item_str_representation(self):
        """
        Test the __str__ method of the Item model.
        """
        item = ItemFactory(title="Test Item")  
        self.assertEqual(str(item), "Test Item") 

    def test_empty_title(self):
        """
        Test that creating an Item with an empty title raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            item = ItemFactory(title="")  
            item.full_clean()  

    def test_empty_description(self):
        """
        Test that creating an Item with an empty description raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            item = ItemFactory(description="")  
            item.full_clean()  

    def test_title_max_length(self):
        """
        Test that the title field cannot exceed 255 characters.
        """
        item = ItemFactory(title="a" * 255)
        item.full_clean()  

        with self.assertRaises(ValidationError):
            item.title = "a" * 256
            item.full_clean()

    def test_timestamps(self):
        """
        Test that created_at and updated_at are automatically set.
        """
        item = ItemFactory()
        self.assertIsNotNone(item.created_at)
        self.assertIsNotNone(item.updated_at)