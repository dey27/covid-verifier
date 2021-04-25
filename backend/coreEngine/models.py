from django.db import models
from taggit.managers import TaggableManager
from django.contrib.postgres.fields import ArrayField


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True,
                               help_text="Auto-Generated Id")
    post_name = models.CharField(max_length=50, blank=False,
                                 help_text="Name of concerned persons, institution, shop etc to be filled here.")
    phone_numbers = ArrayField(models.CharField(max_length=13, blank=True),
                               size=8, help_text="List of comma-separated phone numbers")

    description = models.TextField(max_length=500, blank=True, null=True)
    location_city = models.CharField(max_length=30, blank=False, null=False,
                                     help_text="Name of city")
    location_area = models.CharField(max_length=30, blank=True, null=True,
                                     help_text="Specific area within the city")
    supporting_url = models.URLField(max_length=500, blank=True, null=True,
                                     help_text="Any supporting links for the post.")

    date_created = models.DateTimeField(auto_now_add=True, help_text="Date created in the Database")

    labels = TaggableManager(blank=True)

    def natural_key(self):
        return "{} - {}".format(self.location_city, self.post_name)

    class Meta:
        ordering = ['date_created']
        # name = ['Posts']


class Votes(models.Model):
    vote_id = models.AutoField(primary_key=True,
                               help_text="Auto-Generated Id")
    post = models.ForeignKey(Posts, blank=False, null=False, on_delete=models.CASCADE,
                             help_text="Foreign key to posts.")
    up_vote = models.BooleanField(blank=True, null=True,
                                  help_text="Vote Up if the post is helpful.")
    down_vote = models.BooleanField(blank=True, null=True,
                                    help_text="Vote Down if the post is helpful.")
    note = models.TextField(max_length=20, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date created in the Database")
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.up_vote is not None and self.down_vote is not None:
            raise RuntimeError("Both cannot be voted at same time")
        return super(Posts, self).save(*args, **kwargs)

    def natural_key(self):
        return "{} -> +{}, -{}".format(self.post, self.up_vote, self.down_vote)

    class Meta:
        ordering = ['date_created']
        # name = ['Votes']
