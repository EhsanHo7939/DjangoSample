from django.urls import path
from .views import home, articleDetails, categoryPage, authorPage


app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('home/page/<int:page>/', home, name="home"),
    path('article/<slug:slug>/', articleDetails, name="articleDetails"),
    path('category/<slug:slug>/', categoryPage, name="categoryPage"),
    path('category/<slug:slug>/page/<int:page>/', categoryPage, name="categoryPage"),
    path('author/<slug:username>/', authorPage, name="authorPage"),
    path('author/<slug:username>/page/<int:page>/', authorPage, name="authorPage"),
]