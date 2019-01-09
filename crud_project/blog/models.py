from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #생성될 때 갱신
    updated_at = models.DateTimeField(auto_now=True)#바뀔 때마다 갱신

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'post_id' : self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post)  #coment가 Post가 어떠한 관계가 있는지.
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #1 : n관계에서 외래키를 post에 해도 되는거 아잉교-> n쪽에서 1쪽에서 생성해야돼

    def __str__(self):
        return self.text 

    
class Tag(models.Model):
    post = models.ForeignKey(Post)  #coment가 Post가 어떠한 관계가 있는지. #post_id가 들어감.
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text 


class Product(models.Model):
    
    post = models.ForeignKey(Post)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)