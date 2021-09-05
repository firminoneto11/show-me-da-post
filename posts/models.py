from django.db import models
from django.contrib.auth import get_user_model


class Posts(models.Model):
    author = models.ForeignKey(verbose_name='Author', to=get_user_model(), on_delete=models.CASCADE, null=False,
                               blank=False)
    title = models.CharField(verbose_name='Title', max_length=30, null=False, blank=False)
    post_content = models.CharField(verbose_name='Content', max_length=255, null=False, blank=False)
    posted_on = models.DateTimeField(verbose_name='Posted on', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
        verbose_name = "post"
        verbose_name_plural = "posts"
