from django.test import TestCase, Client
from django.urls import reverse
from ..factories import ItemFactory  

class ItemRedirectViewTest(TestCase):
    def setUp(self):
        """
        Set up data for the tests.
        """
        self.client = Client()
        self.item = ItemFactory()  

    def test_item_redirect_view(self):
        """
        Test that the item_redirect_view redirects to the correct URL.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redirect.html')

    def test_redirect_with_invalid_id(self):
        """
        Test that the item_redirect_view returns a 404 for an invalid item ID.
        """
        invalid_id = 999  
        url = reverse('item_detail', args=[invalid_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_unknown_device(self):
        """
        Test that the item_redirect_view handles unknown devices by redirecting to the web URL.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url, HTTP_USER_AGENT="UnknownDevice/1.0")
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redirect.html')
        self.assertIn('fallback_url', response.context)

    def test_ios_device_redirection(self):
        """
        Test that the item_redirect_view redirects iOS devices to the App Store.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url, HTTP_USER_AGENT="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)")
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('fallback_url', response.context)
        self.assertIn('apps.apple.com', response.context['fallback_url'])

    def test_android_device_redirection(self):
        """
        Test that the item_redirect_view redirects Android devices to the Google Play Store.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url, HTTP_USER_AGENT="Mozilla/5.0 (Linux; Android 10; Pixel 4)")
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('fallback_url', response.context)
        self.assertIn('play.google.com', response.context['fallback_url'])

    def test_web_browser_redirection(self):
        """
        Test that the item_redirect_view redirects web browsers to the item detail page.
        """
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url, HTTP_USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('fallback_url', response.context)
        self.assertIn(f'/item_detail/{self.item.id}/', response.context['fallback_url'])