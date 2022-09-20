from django.test import TestCase

from urllib import response
from django.test import TestCase, Client

from django.urls import reverse

# Create your tests here.
class MyWatchListViewTest(TestCase):

    def test_name_html(self):
        response = self.client.get(reverse('mywatchlist:show_html'))
        self.assertEqual(response.status_code, 200)

    def test_name_xml(self):
        response = self.client.get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code, 200)

    def test_name_json(self):
        response = self.client.get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code, 200)

    def test_url_html(self):
        client = Client()
        response = client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_url_xml(self):
        client = Client()
        response = client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_url_json(self):
        client = Client()
        response = client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)