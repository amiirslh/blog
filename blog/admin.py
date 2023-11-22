from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin
# Register your models here.
admin.sites.AdminSite.site_header=' پنل مدیریت جنگو '
admin.sites.AdminSite.site_title='پنل'
admin.sites.AdminSite.index_title='پنل مدیریت'

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','publish','status']
    ordering = ['title','publish']
    list_filter = ['author','status','publish',]
    list_editable = ['status']
    raw_id_fields = ['author']
    search_fields = ['title','author__username']
    list_display_links = ['title','author']
    date_hierarchy = 'publish'

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['subject','message','name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','name','created','active']
    list_filter =  ['active','created', 'updated']
    search_fields = ['post','name']
    list_editable = ['active']