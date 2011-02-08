from django.db import models

class Release(models.Model):
    version = models.CharField(max_length = 10)
    date = models.DateField()
    change_log = models.TextField()
    description = models.TextField()
    previous_version = models.ForeignKey("Release", blank = True, null = True)

    class Meta:
        ordering = ["date"]
        
    def __unicode__(self):
        return "Version " + self.version
