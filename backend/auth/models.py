from django.db import models


class TokenManager(models.Model):
    """
    Class to store jwt token information for all registered users.
    """
    token_value = models.CharField(max_length=1000)
    token_end_date = models.DateTimeField()

    created_by = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        val = self.token_value[:5] if self.token_value is not None else ''
        end = self.token_end_date if self.token_end_date is not None else ''

        return 'Token<{}> Ends {}'.format(val, end)

    def __repr__(self):
        val = self.token_value[:5] if self.token_value is not None else ''
        end = self.token_end_date if self.token_end_date is not None else ''

        return 'Token<{}> Ends {}'.format(val, end)
