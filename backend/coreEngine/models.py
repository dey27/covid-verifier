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

    """ Votes Logic
    Eventually some posts will grow up to become stale over time.. such posts must have a final negative count.
    It's possible to have a high positive votes, but the last 5 votes be -ve, such posts should bounce below.
    If this won't be created, votes will be stored for last 5 only, but we need to show a better vote count.
    """
    vote_count = models.SmallIntegerField(default=0, null=True, blank=True,
                                          help_text="A total of votes received so far.")

    # created date is not required. A post's worth is determined by last updated timestamp.
    date_updated = models.DateTimeField(auto_now=True, help_text="Last updated timestamp")

    labels = TaggableManager(blank=False)

    def natural_key(self):
        return "{} - {}".format(self.location_city, self.post_name)

    # def save(self, *args, **kwargs):
    #     self.labels.add(kwargs['labels'])
    #     return super(Posts, self).save(*args, **kwargs)

    class Meta:
        ordering = ['date_updated']


class Votes(models.Model):
    """
    Table to only store the voting history, maximum of last 5 histories to reduce DB size.
    """
    vote_id = models.AutoField(primary_key=True,
                               help_text="Auto-Generated Id")
    post = models.ForeignKey(Posts, blank=False, null=False, on_delete=models.CASCADE,
                             help_text="Foreign key to posts.")
    vote = models.BooleanField(default=True, blank=False, null=False,
                               help_text="Vote Up or down on the basis of if post is helpful.")
    note = models.TextField(max_length=20, blank=True, null=True)
    # user_ip = models.GenericIPAddressField(blank=True, null=True,
    #                                        help_text="")
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date created in the Database")

    def save(self, *args, **kwargs):
        if self.vote is True:
            self.post.vote_count = self.post.vote_count + 1
        else:
            self.post.vote_count = self.post.vote_count - 1
        self.post.save()

        return super(Votes, self).save(*args, **kwargs)

    def natural_key(self):
        return "{} -> +{}, -{}".format(self.post, self.up_vote, self.down_vote)

    class Meta:
        ordering = ['date_created']
