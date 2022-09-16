from django.db import models



# Create your models here.
class Driver(models.Model):
    drivername=models.CharField(max_length=20)
    age=models.IntegerField()
    contact_no=models.IntegerField()
    bus_no=models.IntegerField()

    def __str__(self):
        return self.drivername