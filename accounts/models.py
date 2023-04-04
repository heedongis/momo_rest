from django.db import models


class Accounts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']