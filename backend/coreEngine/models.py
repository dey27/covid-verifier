from django.db import models
from taggit.managers import TaggableManager


# class InitiativeManager:
#     def get_by_natural_key(self, initiative_name):
#         return self.get(initiative_name=initiative_name)


class Initiative(models.Model):
    # objects = InitiativeManager()

    initiative_id = models.AutoField(primary_key=True,
                                     help_text="Auto-Generated Id")
    initiative_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)

    workforce_size = models.CharField(max_length=50, blank=True, null=True)
    parent_entity = models.CharField(max_length=100, blank=True, null=True)

    location_city = models.CharField(max_length=50, blank=True, null=True)
    location_country = models.CharField(max_length=50, blank=True, null=True)
    googlemaps_url = models.URLField(max_length=200, blank=True, null=True,
                                     help_text="Map URL of (City, Country) to show on a World Map")

    date_created = models.DateTimeField(auto_now_add=True, help_text="Date created in the Database")
    date_started = models.DateTimeField(auto_now_add=False, blank=True, null=True,
                                        help_text="Project Start Date")
    year_started = models.DateTimeField(auto_now_add=False, blank=True, null=True,
                                        help_text="Project Start Year")

    is_active = models.BooleanField(default=None, null=True,
                                    help_text="Active Status of Initiative")
    labels = TaggableManager(blank=True)

    def natural_key(self):
        return self.initiative_name

    class Meta:
        ordering = ['initiative_id']
