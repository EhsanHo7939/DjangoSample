from django.contrib import admin
from .models import Article, Category

# Admin Panel Header
admin.site.site_header = "Cactus 🌵🖤"

# Panel Actions

## Globally disable delete selected
admin.site.disable_action('delete_selected')

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "1 article was"
    else:
        message_bit = "{0} articles were".format(rows_updated)
    modeladmin.message_user(request, "{0} successfully marked as published.".format(message_bit))
make_published.short_description = "Publish selected Articles"

def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "1 article was"
    else:
        message_bit = "{0} articles were".format(rows_updated)
    modeladmin.message_user(request, "{0} successfully marked as draft.".format(message_bit))
make_draft.short_description = "Draft selected Articles"

def activate_category(modeladmin, request, queryset):
    rows_updated = queryset.update(status=True)
    if rows_updated == 1:
        message_bit = "1 category was"
    else:
        message_bit = "{0} categories were".format(rows_updated)
    modeladmin.message_user(request, "{0} successfully marked as active.".format(message_bit))
activate_category.short_description = "Activate selected Categories"

def deactivate_category(modeladmin, request, queryset):
    rows_updated = queryset.update(status=False)
    if rows_updated == 1:
        message_bit = "1 category was"
    else:
        message_bit = "{0} categories were".format(rows_updated)
    modeladmin.message_user(request, "{0} successfully marked as deactive.".format(message_bit))
deactivate_category.short_description = "Deactivate selected Categories"



# Admin Panels
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')

    actions = [activate_category, deactivate_category]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','author','jDateTime','status','category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title','slug','description')    
    ordering = ('status', '-publish')

    actions = [make_published, make_draft]




# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
