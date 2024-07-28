from django.forms import ModelForm
from main.models import Article
#from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields=["title", "text"]