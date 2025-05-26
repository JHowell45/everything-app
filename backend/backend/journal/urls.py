from django.urls import path

from .views import IndexView
from . import views

app_name = 'journal'

urlpatterns = [
    path("", IndexView.as_view(), name ="index"),
    path("entry", views.new_entry, name="new_entry"),
]