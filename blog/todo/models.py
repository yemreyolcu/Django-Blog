from django.db import models



class todoForm(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title : ")
    description = models.TextField(max_length=250,verbose_name="Description : ")
    is_finished = models.BooleanField(default=False,verbose_name="Is Finished ? ")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
# Create your models here.
