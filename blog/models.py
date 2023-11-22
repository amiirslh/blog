from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from django_jalali.db import models as jmodels
from django.urls import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.Published)

class Post(models.Model):
    class Status(models.TextChoices):
        Published='PB','Published'
        Draft='DR','Draft'
        Rejected='RJ','Rejected'

    #author info
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts',verbose_name='نویسنده')

    #datafield

    title=models.CharField(max_length=200)
    description=models.TextField()
    slug=models.SlugField(max_length=250)

    #date and time info
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    #chioces
    status=models.CharField(max_length=2,choices=Status.choices,default='DR')
    reading_time=models.PositiveIntegerField(verbose_name='زمان مطالعه')

    #objects=models.Manager()
    #objects=jmodels.jManager()
    published=PublishedManager()



    class Meta:
        ordering=['publish']
        indexes=[
            models.Index(fields=['publish'])
        ]
        verbose_name='پست ها '
        verbose_name_plural='پست ها'


    def __str__(self):
        return self.title

    def get_absolutue_url(self):
        return reverse('blog:post_details',args=[self.id])
    def get_url(self):
        return reverse('blog:posts_list')

class Ticket(models.Model):

    message = models.TextField(verbose_name=" پیام")
    name=models.CharField(max_length=150,verbose_name='نام')
    email=models.EmailField(verbose_name='ایمیل')
    phone=models.CharField(max_length=15,verbose_name='شماره  تماس')
    subject=models.CharField(max_length=150)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'تیکت  '
        verbose_name_plural = 'تیکت ها'


class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments',verbose_name='کامنت')
    name=models.CharField(max_length=250,verbose_name='نام')
    body=models.TextField(verbose_name='نظر')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=False)

    class Meta:
        ordering=['created']
        indexes = [
            models.Index(fields = ['created'])
        ]

        verbose_name='نظر'
        verbose_name_plural='نظرات'

    def __str__(self):
        return f'{self.name}:{self.post}'

