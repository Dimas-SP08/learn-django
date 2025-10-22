from django.db import models

# Create your models here.

class Publication(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=250)
    fill = models.TextField(null=True)
    OPTION_CATAGORY= [
        ('python','python'),
        ('django','django'),
        ('javascript','javascript'),
    ]
    categories = models.CharField(max_length=50,choices=OPTION_CATAGORY)
    publications = models.ForeignKey(Publication, on_delete=models.CASCADE,null=True,  blank=True  )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
class Readlist(models.Model):
    readers = models.ForeignKey(Reader, on_delete=models.CASCADE)
    articles = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.articles.title} - {self.readers.name}'