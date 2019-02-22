from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=25)
    last_name   = models.CharField(max_length=25)
    date_added = models.CharField(max_length=10)
    deleted_on = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ('user_name', 'password', 'first_name', 'last_name', 'date_added', 'deleted_on' )

class Deck(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.CharField(max_length=10)
    deleted_on = models.CharField(max_length=10)
    trainer = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='decks')

    def __str__(self):
        return self.name

# Create your models here.
