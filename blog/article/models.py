from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Article",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="name")
    comment_content = models.CharField(max_length=200,verbose_name="comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_author
    class Meta:
        ordering = ['-comment_date']
