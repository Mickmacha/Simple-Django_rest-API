from django.db import models


    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.name
class Beverages(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # image = models.ImageField(upload_to='images/')
    category = models.ForeignKey('Category', related_name="beverages", on_delete=models.CASCADE)
    
    @classmethod
    def get_all_beverages(cls):
        return cls.objects.all()
    
    def __str__(self):
        return self.name