from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from .mixins import (
    FieldsMixin,
    FormValidMixin,
    AuthorAccessMixin,
    SuperUserAccessMixin,
    AuthorsAccessMixin,
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from blog.models import Article
from .forms import ProfileForm


# Create your views here.

class ArticleList(AuthorsAccessMixin, ListView):
    template_name = "registration/userHome.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(AuthorsAccessMixin, FieldsMixin, FormValidMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdate(AuthorAccessMixin, FieldsMixin, FormValidMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleDelete(SuperUserAccessMixin, FieldsMixin, FormValidMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:userHome')
    template_name = "registration/article-delete.html"


class Profile(LoginRequiredMixin ,UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("account:profile")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or user.is_author:
            return reverse_lazy('account:userHome')
        else:
            return reverse_lazy('account:profile')

