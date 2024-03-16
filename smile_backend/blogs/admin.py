from django.contrib import admin

# Register your models here.
from .models import Author, b_post, Comment,ContentBlock

admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(b_post)
admin.site.register(ContentBlock)
