from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    categorydescription = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_description_summary(self):
        max_length = 50
        if len(self.categorydescription) > max_length:
            return f"{self.categorydescription[:max_length]}..."
        return self.categorydescription
