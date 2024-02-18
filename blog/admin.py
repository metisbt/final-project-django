from django.contrib import admin
from blog.models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_view', 'status', 'login_require', 'published_date', 'created_date')
    list_filter = ('status','author')
    # ordering = ('-created_date',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('post','approved')
    search_fields = ['name', 'post']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
# admin.site.register(Post, PostAdmin)
