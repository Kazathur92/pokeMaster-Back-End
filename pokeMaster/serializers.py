from rest_framework import serializers
from pokeMaster.models import Deck, User, Card, DeckCardsRelationship
from rest_framework.authtoken.models import Token
# from rest_framework.field import CurrentUserDefault


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'password', 'first_name', 'last_name','email', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined',  'url')

class DeckSerializer(serializers.HyperlinkedModelSerializer):
    # director = DirectorSerializer(read_only=True)

    class Meta:
        model = Deck
        fields = ('id','name', 'description', 'strategy', 'date_added', 'deleted_on', 'url', 'imageCover1', 'imageCover2', 'imageCover3', 'imageCover4', 'imageMvp','user')
        # fields = "__all__"


class CardSerializer(serializers.HyperlinkedModelSerializer):
    DeckSerializer(many=True, source='deck.all', read_only=True)

    class Meta:
        model = Card
        fields = ("id", "cardId", "deck", "deleted", "imageUrl", "imageUrlHiRes", "name", "rarity", "url", "user")
        # fields = "__all__"

class TrainerDecksRelationshipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class DeckCardsRelationshipSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = DeckCardsRelationship
        # fields = "__all__"
        fields = ("id", "cardId", 'card', 'deck')

class GamesPlayedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class TokenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = "__all__"
        model = Token
