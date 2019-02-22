from rest_framework import serializers
from movies.models import Deck, User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'user_name', 'password', 'first_name', 'last_name', 'date_added', 'deleted_on')

class DeckSerializer(serializers.HyperlinkedModelSerializer):
    # director = DirectorSerializer(read_only=True)

    class Meta:
        model = Deck
        fields = ('id', 'url', 'name', 'date_added', 'deleted_on')
        # fields = "__all__"