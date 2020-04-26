from django.db import models


class Article(models.Model):
    article_id = models.AutoField(primary_key=True,
                                  help_text="Auto-Generated Id")

    title = models.CharField(max_length=200, blank=False, null=False)
    url = models.URLField(max_length=200, blank=False, null=False)
    article_text = models.TextField(max_length=1000, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_crawled = models.DateTimeField(auto_now_add=False, blank=False, null=False)
    date_published = models.DateTimeField(auto_now_add=False, blank=False, null=False)

    is_processed = models.BooleanField(default=False, null=False,
                                       help_text="Whether the article_text is processed for initiatives or not.")

    def natural_key(self):
        return self.article_id

    class Meta:
        ordering = ['date_created']
        unique_together = ['url']
