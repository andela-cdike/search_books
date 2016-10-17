from django.db import models


class Book(models.Model):
    '''Defines the book object'''
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=25)
    pub_date = models.DateField()

    def __unicode__(self):
        return self.title
