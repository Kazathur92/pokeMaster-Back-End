from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from movies import views


router = DefaultRouter()
router.register('users', views.MovieViewSet)
router.register('decks', views.DirectorViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]


