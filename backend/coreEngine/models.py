from django.db import models

class InitiativeManager():
    def get_by_natural_key(self, name):
        return self.get(name=fullname)

class Initiative(models.Model):
    objects = InitiativeManager()
    
    initiative_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=False)

    added_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def natural_key(self):
        return (self.name)

    class Meta:
        ordering = ['initiative_id']
