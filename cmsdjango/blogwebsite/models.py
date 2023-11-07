from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS=(
    (0,'Draft'),
    (1,'Publish'),
    (2,'Delete')
)

class posts(models.Model):
    title=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    # publication_date=models.DateTimeField()
    # publication_date=models.DateTimeField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField()
    content=models.TextField()
    metades = models.CharField(max_length=300, default="new post")
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
    ordering=['created_on']

def __str__(self):
    return self.title
