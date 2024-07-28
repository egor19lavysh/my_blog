from django.urls import path
from . import views

app_name = "write"

urlpatterns = [
    path("create_article/", views.create, name="create_article"),
]