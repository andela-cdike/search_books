from django.http import QueryDict
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone


class SearchViewTestSuite(TestCase):
    '''Tests for search view and functionality'''

    def setUp(self):
        self.book = Book.objects.create(
            title='Knightmare Academy',
            category='thriller',
            date_published=timezone.now()
        )
        self.client = Client()

    def test_get_search_view(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_for_book(self):
        query_dict = QueryDict('', mutable=True)
        query_dict.update({'q': 'academy'})
        url = '{base_url}?{query_string}'.format(
            base_url=reverse('search'),
            query_string=query_dict.urlencode()
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Knightmare Academy', response.content)
