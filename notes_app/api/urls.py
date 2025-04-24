from django.urls import path, include
from .views import NotesViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'notes', NotesViewSet)

urlpatterns = [
    path('', include(router.urls))
]

