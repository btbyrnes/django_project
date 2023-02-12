from django.db import models


class MenuItem(models.Model):
   title = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
   inventory = models.SmallIntegerField(default=0)

   def __str__(self):
      return f"{self.title} : {str(self.price)}"

