from django.db import models

class Description(models.Model):
    class_id = models.CharField(max_length=200)
    class_name = models.CharField(max_length=200)
    description_text = models.CharField(max_length=2000)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.class_name