from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Столик #{self.number} (мест: {self.seats})"

