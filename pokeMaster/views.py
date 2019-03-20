from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from pokeMaster.models import Deck
from pokeMaster.models import Card
from pokeMaster.models import DeckCardsRelationship
from pokeMaster.serializers import DeckSerializer
from pokeMaster.serializers import CardSerializer
from pokeMaster.serializers import UserSerializer
from pokeMaster.serializers import DeckCardsRelationshipSerializer
from pokeMaster.serializers import TokenSerializer





@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    email=req_body['email'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'],
                    )

    # Use the REST Framework's token generator on the new user account
    # This is the same as calling a method for loggin in a user after you create their account
    token = Token.objects.create(user=new_user)
    # print("REQUEST: ", request.__dict__)
    print("REQUEST BODY: ", request.body)
    # Return the token to the client
    data = json.dumps({"token":token.key})
    return HttpResponse(data, content_type='application/json')



class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']


    def get_queryset(self):

        print("USER 1", self.request.__dict__)
        print("USER 1", self.request.auth)



        if self.request.auth is None:
            allDecks = Deck.objects.all()
            return allDecks

        else:
            print(self.request.method )
            print("USER", self.request.user)
            user = self.request.user
            userDecks = Deck.objects.filter(user=user)

            return userDecks


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    print("HELLO")

    def destroy(self, request, *args, **kwargs):
        print("INSIDE DESTROY")
        print("SELF", self)
        print("QUERY", self.request.query_params)
        print("REQUEST", request.__dict__)
        print("ARGS", args)
        print("KWARGS", kwargs['pk'])

        card_id = kwargs['pk']
        card = Card.objects.get(pk=card_id)
        card.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):


        if self.request.auth is None:
            allCards = Card.objects.all()
            return allCards

        else:
            print("USER", self.request.user)
            user = self.request.user
            userCards = Card.objects.filter(user=user)
            return userCards

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserIdViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        print("USER ID: ", self.request.user.id)
        return User.objects.filter(id=self.request.user.id)

class DeckCardRelationshipForIdViewSet(viewsets.ModelViewSet):
    queryset = DeckCardsRelationship.objects.all()
    serializer_class = DeckCardsRelationshipSerializer

    def destroy(self, request, *args, **kwargs):
        print("WOOHO")

        cardApiId = request.query_params['card']
        deckId = self.request.parser_context['kwargs']['pk']
        print("CARD API ID", cardApiId)
        print("DECK ID", deckId)

        cardInRelationship = DeckCardsRelationship.objects.filter(cardId=cardApiId, deck=deckId)[0]
        print("CARD ID IN CARDS", cardInRelationship.card_id)
        cardDb_id = cardInRelationship.card_id
        print("cardDb_id")
        cardInCards = get_object_or_404(Card, pk=cardDb_id)
        print("THE CARD", cardInCards.__dict__)
        cardInCards.delete()
        cardInRelationship.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class DeckCardRelationshipViewSet(viewsets.ModelViewSet):
    queryset = DeckCardsRelationship.objects.all()
    serializer_class = DeckCardsRelationshipSerializer


    def get_queryset(self):

        print("REQUEST", self.request.query_params['filter'])
        deckUrl = self.request.query_params['filter']

        userCards = DeckCardsRelationship.objects.filter(deck=deckUrl)
        print("USER CARDS: " , userCards)

        return userCards


    def destroy(self, request, *args, **kwargs):

        print("REQUEST DICTIONARY", request.__dict__)
        print("REQUEST", self.request.parser_context['kwargs']['pk'])
        print("REQUEST: ", request.query_params)
        print("REQUEST: ", request.query_params['card'])


        cardApiId = request.query_params['card']
        deckId = self.request.parser_context['kwargs']['pk']

        cardInDatabase = DeckCardsRelationship.objects.filter(cardId=cardApiId, deck_id=deckId)[0]

        print("CARD", cardInDatabase)
        cardInDatabase.delete()


        return Response(status=status.HTTP_204_NO_CONTENT)
        # return


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer




# Create your views here.
