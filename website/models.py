from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)

    class Meta:
        # app_label

        # more usef
        ordering = ['-created_date']

    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email