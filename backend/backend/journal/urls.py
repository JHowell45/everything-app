from django.urls import path

from .views import IndexView
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name ="index"),
    path("/<int:entry_id>/entry", views.new_entry, name="new_entry"),
]