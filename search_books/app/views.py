from django.db.models import Q
from django.views.generic.list import ListView

from app.model import Book


class SearchView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'app/index.html'

    def get_queryset(self):
        '''
        Modify queryset in include only results that match search criteria
        '''
        queryset = super(SearchView, self).get_queryset()
        query_string = self.request.GET.get('q', '')
        queryset = queryset.filter(
            Q(title__icontains=query_string) |
            Q(category__icontains=query_string)
        )
        return queryset
