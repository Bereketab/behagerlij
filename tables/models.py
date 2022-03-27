from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import AbstractUser

class Table(models.Model):
    table_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('table-update', kwargs={'pk': self.pk})

    def __str__(self):
        return self.table_name

class Feilds(models.Model):
    tables = models.ForeignKey(Table, on_delete = models.CASCADE)
    field_name = models.CharField(max_length=20)
    field_data_type = models.CharField(max_length=20)
    field_max_length = models.CharField(max_length=20)
    
    def __str__(self):
        return self.field_name


