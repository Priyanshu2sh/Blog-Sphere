from django.contrib import admin
from .models import *

# Register your models here.
class TagTublerinline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerinline]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mobile','image']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)