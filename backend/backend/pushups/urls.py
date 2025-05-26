from django.urls import path
from .views import IndexView

app_name = "pushups"

urlpatterns = [
    path("", IndexView.as_view(), name="index")
]