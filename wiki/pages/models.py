from django.db import models
from time import time


class Page(models.Model):
    title = models.CharField(max_length=200)
    name = ''
    history = []
    last_change_time = models
    article = models.TextField()

    def __str__(self):
        return self.title + (' %d symbols' % len(self.article))

    def change(self, n_article):
        self.history += [self.article]
        self.article = n_article

    #create_date = models.DateTimeField('date created')
    #author = models.CharField(max_length=200)
