from django.test import TestCase
from django.utils import timezone

from app.models import Book

class BookTestSuite(TestCase):
    '''Tests for the Book model'''
    def setUp(self):
        self.book = Book.objects.create(
            title='Knightmare Academy',
            category='thriller',
            date_published=timezone.now()
        )

    def test_book_model(self):
        book = Book.objects.all()[0]
        self.assertEqual(str(book), self.book.title)
