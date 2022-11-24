from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    position = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='users',null=True,blank=True)
    
class Service(models.Model):
    image = models.ImageField(upload_to="service")
    name = models.CharField(max_length=200)
    info = models.TextField()

    def __str__(self):
        return self.name

class ClientWord(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Team(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="team")
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def comments(self):
        return Comments.objects.filter(post__title=self.title).all()

    def __str__(self):
        return self.title
    
class Statistika(models.Model):
    name = models.CharField(max_length=100)
    nums = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question

class Statistika(models.Model):
    name = models.CharField(max_length=100)
    nums = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title

