from django.contrib import admin

# Register your models here.
from .models import Author, b_post, Comment,ContentBlock,Team,Event,Quote,Yvideos,Image,ImgGrp

admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(b_post)
admin.site.register(ContentBlock)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Quote)
admin.site.register(Yvideos)
admin.site.register(ImgGrp)
admin.site.register(Image)
