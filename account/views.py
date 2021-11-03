from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Article


# Create your views here.

class ArticleList(LoginRequiredMixin, ListView):
    queryset = Article.objects.all()
    template_name = "registration/userHome.html"