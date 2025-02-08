from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ..factories import ItemFactory  
from ..serializers import ItemDetailSerializer

class ItemDetailSerializerTest(TestCase):
    def setUp(self):
        """
        Set up data for the tests.
        """
        self.item = ItemFactory()  
        self.factory = APIRequestFactory()

    def test_item_detail_serializer(self):
        """
        Test that the ItemDetailSerializer returns the expected data.
        """
        request = self.factory.get('/')
        serializer = ItemDetailSerializer(
            instance=self.item,
            context={'request': request}
        )
        expected_data = {
            'id': self.item.id,
            'title': self.item.title, 
            'description': self.item.description,  
            'share_link': f"http://testserver/item_detail/{self.item.id}/"
        }
        self.assertEqual(serializer.data, expected_data)

    def test_serializer_with_empty_title(self):
        """
        Test that the ItemDetailSerializer handles empty titles correctly.
        """
        item = ItemFactory(title="")
        request = self.factory.get('/')
        serializer = ItemDetailSerializer(
            instance=item,
            context={'request': request}
        )
        self.assertEqual(serializer.data['title'], "")