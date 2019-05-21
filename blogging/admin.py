from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'Author')
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')


# admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
