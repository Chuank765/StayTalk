from django.db import models

class BoardUnit(models.Model):
    name = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=2, default='m', null=False)
    subject = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, blank=True, default='')
    web = models.CharField(max_length=200, blank=True, default='')
    content = models.TextField(null=False)
    response = models.TextField(blank=True, default='')
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject