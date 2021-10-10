from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title


    def summary(self):
        if len(self.body) > 100:
            return self.body[:100]+'...'
        else:
            return self.body