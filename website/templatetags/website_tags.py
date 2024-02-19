from django import template
from blog.models import Post, Comment
from django.utils import timezone
from datetime import datetime, timezone

register = template.Library()

@register.inclusion_tag('website/latest-post-home.html')
def latest_post_home():
    posts = Post.objects.filter(published_date__lte=datetime.now(tz=timezone.utc), status=1).order_by('-published_date')[:6]
    return {'posts' : posts}

@register.inclusion_tag('website/latest-comment-home.html')
def latest_comment_home():
    comment = Comment.objects.filter(approved=True).order_by('-created_date')[:4]
    return {'comment' : comment}
