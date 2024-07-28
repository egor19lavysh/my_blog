from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
     path("", views.ArticlesList.as_view(), name="index"),
     path("<int:pk>/", views.ArticleDetail.as_view(), name="detail"),
]