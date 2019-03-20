from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE



class Deck(SafeDeleteModel):
    """A deck that a user can add cards to"""
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=800, null=True)
    strategy = models.CharField(max_length=800, null=True)
    date_added = models.CharField(max_length=10)
    deleted_on = models.CharField(max_length=10, null=True)
    maxCardAmmount = models.IntegerField(default=60)
    imageCover1 = models.CharField(max_length=100, null=True)
    imageCover2 = models.CharField(max_length=100, null=True)
    imageCover3 = models.CharField(max_length=100, null=True)
    imageCover4 = models.CharField(max_length=100, null=True)
    energyType1 = models.CharField(max_length=100, null=True)
    energyType2 = models.CharField(max_length=100, null=True)
    energyType3 = models.CharField(max_length=100, null=True)
    energyType4 = models.CharField(max_length=100, null=True)
    imageMvp = models.CharField(max_length=100, null=True)
    mvpName = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class Card(SafeDeleteModel):
    """A card that a user can add to their collection"""
    _safedelete_policy = SOFT_DELETE_CASCADE
    cardId = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=50)
    imageUrlHiRes = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='trainer')
    deck =  models.ManyToManyField('Deck', blank=True, through='DeckCardsRelationship')


    def __str__(self):
        return self.name



class DeckCardsRelationship(models.Model):
    cardId = models.CharField(max_length=50)
    card = models.ForeignKey('Card', on_delete=models.CASCADE, null=True)
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE, null=True)



class GamesPlayed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True)
    date_added = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.status
# Create your models here.
