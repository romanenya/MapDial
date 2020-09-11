from django.db import models

# Create your models here.
class Chronology(models.Model):
    title = models.TextField()
    date = models.DateField()
    file = models.ImageField(upload_to='chronology')

    def __str__(self):
        return self.title + ' --- ' + str(self.date)