from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .mixins import (
    FieldsMixin,
    FormValidMixin,
    AuthorAccessMixin,
    SuperUserAccessMixin,
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from blog.models import Article


# Create your views here.

class ArticleList(LoginRequiredMixin, ListView):
    template_name = "registration/userHome.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FieldsMixin, FormValidMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdate(AuthorAccessMixin, FieldsMixin, FormValidMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleDelete(SuperUserAccessMixin, FieldsMixin, FormValidMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:userHome')
    template_name = "registration/article-delete.html"


class Profile(UpdateView):
    model = User
    template_name = "registration/profile.html"
    fields = [
        'username',
        'email',
        'first_name',
        'last_name',
        'VIP_user',
        'is_author',
        'date_joined',
    ]
    success_url = reverse_lazy("account:profile")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

