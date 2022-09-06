from django.db import models


# Create your models here.
# django documentation is a resource for detailed illustration of the model classes, including
# using fields as foreign keys
class ProductApp(models.Model):
    name = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()

    # This is to override the string object. Without this, the item would show
    # ProductApp object. Now, it shows the name of the object, as assigned
    def __str__(self):
        return self.name
