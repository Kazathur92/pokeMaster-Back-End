from django.conf.urls import include, url
# from django.urls import path
from rest_framework.routers import DefaultRouter
from pokeMaster import views
# from django.conf.urls import url
from django.urls import path

from . import views

# app_name = 'pokeMaster'

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('decks', views.DeckViewSet)
router.register('cards', views.CardViewSet)
router.register('deckcardsrelationship', views.DeckCardRelationshipViewSet)
router.register('findRelationship', views.DeckCardRelationshipForIdViewSet)
router.register('tokens', views.TokenViewSet)
router.register('user-id', views.UserIdViewSet, base_name="UserId")


# router.register('decks/{deck_id}/cards/{card_id}/', views.DeckCardRelationshipViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls )),
]



# is the username and password being hashed when sent or when saved in database?