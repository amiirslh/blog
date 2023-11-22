from ..models import*
from django import template
from django.db.models import Sum , Max , Min ,Avg,Count
from markdown import markdown
from django.utils.safestring import  mark_safe
register = template.Library()

@register.simple_tag()
def posts_number():
    post_number = Post.published.count()
    return post_number

@register.simple_tag()
def comment_count():
    activec=Comment.objects.filter(active=True).count()
    noneavtivec = Comment.objects.filter(active=False).count()
    allc = Comment.objects.all().count()
    return f'active: {activec}, None_active: {noneavtivec}, all : {allc}'

@register.simple_tag()
def lastp(count=3):
    return Post.published.last().publish




@register.inclusion_tag('partials/latest_posts.html')
def latest_posts(count=4):

    lposts2=Post.published.order_by('publish')[:count]
    context={
        'lposts2':lposts2
    }
    return context

@register.simple_tag
def readingtimesum():
    rt=Post.published.aggregate(Sum('reading_time'))
    return rt['reading_time__sum']

@register.simple_tag
def most_pop_posts(count=4):
    mp=Post.published.annotate(comments_count=Count("comments")).order_by('-comments_count')[:count]
    return mp


@register.filter(name='markdown')
def to_markdown(text):
    return mark_safe(markdown(text))


@register.simple_tag()
def lapo(count=5):
    lpt=Post.published.order_by('publish')[:count]
    return lpt