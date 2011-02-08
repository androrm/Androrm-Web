from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 80)
    description = models.TextField(blank = True)
    parent = models.ForeignKey("Category", blank = True, null = True)
    url = models.CharField(max_length = 50)
    position = models.IntegerField(null = True)
    
    class Meta:
        ordering = ["position"]
    
    def __unicode__(self):
        return self.name + " at: " + self.get_url()
        
    def get_url(self):
        if self.parent:
            return self.parent.get_url() + self.url
            
        return "/" + self.url
        
class Author(models.Model):
    name = models.CharField(max_length = 80)      
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name

class Entry(models.Model):
    headline = models.CharField(max_length = 80)
    content = models.TextField()
    author = models.ForeignKey("Author")
    date = models.DateField()
    published = models.BooleanField()
    categories = models.ManyToManyField("Category")
    
    def __unicode__(self):
        return self.headline + " by " + self.author.name