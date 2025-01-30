from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    #модель - класс описания предмета

    def __str__(self):
        return self.title

