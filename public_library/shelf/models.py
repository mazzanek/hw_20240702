from django.db import models

class Book(models.Model):
    bookname = models.CharField(max_length=255)
    writername = models.CharField(max_length=255)