from django.db import models
from account.models import User
from django.urls import reverse
from django.utils import timezone
from extensions.utils import jalali_datetime
from django.utils.html import format_html





# Custom Managers

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')




class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)




# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True, verbose_name="Active?")
    position = models.IntegerField(verbose_name="position")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['position']

    def __str__(self):
        return self.title

    objects = CategoryManager()




class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('i', 'Investigating'),
        ('r', 'Returned'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articles", verbose_name="Author")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, verbose_name="Category", related_name="articles")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-publish"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("account:userHome")

    def jDateTime(self):
        return jalali_datetime(self.publish)
    jDateTime.short_description = "Date & Time"

    def thumbnail_tag(self):
        return format_html("<img width=100 height=70 style='border-radius: 5px;' src='{0}'".format(self.thumbnail.url))
    thumbnail_tag.short_description = "Thumbnail"

    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])
    category_to_str.short_description = "Category"

    objects = ArticleManager()