from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.SearchView.as_view(), name='search')
]
