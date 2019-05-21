from django.contrib import admin
from blogging.models import Post, Category, Topic


class CategoryInline(admin.TabularInline):
    model = Topic
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInline, )


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
