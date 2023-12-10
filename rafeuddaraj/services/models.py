from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=50)
    logo = models.URLField()
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Services"
    
    def __str__(self) -> str:
        return self.name
class Portfolio(models.Model):
    title = models.TextField()
    image = models.URLField()
    description = models.TextField()
    live_link = models.URLField()
    repos_link = models.URLField()
    class Meta:
        verbose_name_plural = "Portfolios"
    
    def __str__(self) -> str:
        return self.title
    
class Resume(models.Model):
    name = models.TextField()
    subTitle = models.TextField()
    image = models.URLField()
    date = models.DateTimeField()
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Resumes"
    
    def __str__(self) -> str:
        return self.name
    
class Package(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural = "Packages"
    
    def __str__(self) -> str:
        return self.name
    

class Client(models.Model):
    name = models.TextField()
    company_name = models.TextField()
    position = models.CharField(max_length=20)
    logo = models.URLField()
    link = models.URLField()
    
    class Meta:
        verbose_name_plural = "Clients"
    
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return self.name
    

class ClientsReview(models.Model):
    clients = models.ForeignKey(to=Client,related_name='client',on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "ClientReviews"
    
    def __str__(self) -> str:
        return self.clients


class Blog(models.Model):
    user = models.ForeignKey(to=User,related_name='blog_user',on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    like = models.PositiveIntegerField()
    like = models.PositiveIntegerField()
    slug = models.SlugField(editable=False,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    
    def save(self,*args,**kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Blogs"
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(to=User,related_name='comment_user',on_delete=models.CASCADE)
    blog = models.ForeignKey(to=Blog,on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_created=True)
    class Meta:
        verbose_name_plural = 'Comments'
    def __str__(self) -> str:
        return self.comment
    