from django.contrib import admin
from .models import Author, Post, Cathegory, Comment, PostCathegory, SubscribersCathegory
# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Cathegory)
admin.site.register(Comment)
admin.site.register(PostCathegory)
admin.site.register(SubscribersCathegory)