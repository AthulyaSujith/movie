from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    imgs = models.ImageField(upload_to='gallery')
    year = models.IntegerField()

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
