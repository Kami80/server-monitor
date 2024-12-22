from django.db import models

class Metric(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
