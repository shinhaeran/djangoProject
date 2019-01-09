from django.contrib import admin
from .models import Post, Comment ,Tag,Product
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at']
    search_fields= ['title',]

# admin.site.register(Post , PostAdmin) 위에 3줄이랑 똑같음 위에는 커스터마이징 가능
# admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','text','created_at','post_id']
    # search_fields= ['title',]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','text','created_at','post_id']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','quantity','price']