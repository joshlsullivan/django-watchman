from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    watchman_group_id = models.CharField(max_length=120, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

class EmailSent(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)
