from django.db import models

# Create your models here.
class Skills(models.Model):
    id=models.IntegerField(primary_key=True)
    skill=models.CharField(max_length=30)
    relevant=models.BooleanField(default=False)

    def __str__(self) :
        return self.skill

class Projects(models.Model):
    title=models.CharField(max_length=30)
    img=models.ImageField(upload_to='static/images')
    deploy_link=models.URLField(blank=True,unique=True)
    github_link=models.URLField(blank=True,unique=True)
    youtube_link=models.URLField(blank=True,unique=True)
    about=models.TextField(max_length=None)
    category=models.ManyToManyField(Skills)

    
    def __str__(self):
        return self.title


    

    

    

    
