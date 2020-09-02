"""Modelos de Tienda Libros"""
from django.db import models


class Author(models.Model):
    """Create Model Table of the author"""
    name = models.CharField(max_length=50, blank = False, null = False)
    last_name = models.CharField(max_length=50, blank = False, null = False)
    nationality = models.CharField(max_length=50, blank = False, null = False)
    description = models.TextField(blank= False, null= False)
