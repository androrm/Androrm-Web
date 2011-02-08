from django.db import models

class BugReport(models.Model):
    STATUS = (
        ("Reported", "reported")[::-1],
        ("Accepted as bug", "accepted")[::-1],
        ("Rejected", "rejected")[::-1],
        ("Duplicate", "duplicate")[::-1],
        ("Work in porgress", "in_progress")[::-1],
        ("Fixed", "fixed")[::-1],
        ("Won't fix", "wont_fix")[::-1]
    )
    
    SEVERITY = (
        ("Low", "low")[::-1],
        ("Medium", "medium")[::-1],
        ("High", "high")[::-1],
        ("Pain in the arse", "extreme")[::-1]
    )
    
    overview = models.CharField(max_length = 150)
    description = models.TextField()
    author = models.ForeignKey("User")
    reported_on = models.DateField()
    accepted = models.BooleanField(default = False)
    open = models.BooleanField(default = True)
    status = models.CharField(max_length = 50, choices = STATUS)
    severity = models.CharField(max_length = 50, choices = SEVERITY)
    last_changed = models.DateField()
    comments = models.ManyToManyField("Comment")
    
    def __unicode__(self):
        return "Bug reported by " + self.author + " on " + self.date
        
class FeatureRequest(models.Model):
    STATUS = (
        ("Submitted", "submitted")[::-1],
        ("Accepted", "accepted")[::-1],
        ("Rejected", "rejected")[::-1],
        ("Work in progress", "in_progress")[::-1],
        ("Implemented", "implemented")[::-1],
        ("Won't implement", "wont_implement")[::-1]
    )
    
    overview = models.CharField(max_length = 150)
    description = models.TextField()
    author = models.ForeignKey("User")
    filed = models.DateField()
    accepted = models.BooleanField(default = False)
    status = models.CharField(max_length = 50, choices = STATUS)    
    last_changed = models.DateField()
    comments = models.ManyToManyField("Comment")
    
    def __unicode__(self):
        return "Feature Request by " + self.author.name + " on " + self.date  

class Comment(models.Model):
    author = models.ForeignKey("User")
    content = models.TextField()
    date = models.DateField()
    
    def __unicode__(self):
        return "Comment from " + self.user.name + " on " + self.bug.overview[0:30]

class User(models.Model):
    name = models.CharField(max_length = 80)
    password = models.CharField(max_length = 56)
    email = models.EmailField()
    blacklisted = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.name + "(" + self.email + ")"