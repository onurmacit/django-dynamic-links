from django.test import TestCase, Client
from django.urls import reverse
from ..factories import ItemFactory  

class ItemIntegrationTest(TestCase):
    def setUp(self):
        """
        Set up data for the tests.
        """
        self.client = Client()
        self.item = ItemFactory()  

    def test_ios_device_redirection(self):
        """
        Test that iOS devices are redirected to the App Store.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url, HTTP_USER_AGENT="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redirect.html')
        self.assertIn('fallback_url', response.context)
        self.assertIn('apps.apple.com', response.context['fallback_url'])

    def test_android_device_redirection(self):
        """
        Test that Android devices are redirected to the Google Play Store.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url, HTTP_USER_AGENT="Mozilla/5.0 (Linux; Android 10; Pixel 4)")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redirect.html')
        self.assertIn('fallback_url', response.context)
        self.assertIn('play.google.com', response.context['fallback_url'])

    def test_web_browser_redirection(self):
        """
        Test that web browsers are redirected to the item detail page.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url, HTTP_USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redirect.html')
        self.assertIn('fallback_url', response.context)
        self.assertIn(f'/item_detail/{self.item.id}/', response.context['fallback_url'])

    def test_invalid_item_id(self):
        """
        Test that invalid item IDs return a 404 error.
        """
        invalid_item_id = 999  
        url = reverse('item_detail', args=[invalid_item_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_custom_domain(self):
        """
        Test that the fallback_url uses the correct domain.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url, HTTP_HOST='example.com')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fallback_url', response.context)
        self.assertIn('example.com', response.context['fallback_url'])

    def test_item_with_long_title(self):
        """
        Test that items with long titles are handled correctly.
        """
        item = ItemFactory(title="a" * 255)
        url = reverse('item_detail', args=[item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redirect.html')