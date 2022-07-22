from django.db import models

class Board(models.Model):
    base_name = models.CharField(max_length=20, null=False)
    base_gender = models.CharField(max_length=2, default='m', null=False)
    base_subject = models.CharField(max_length=100, null=False)
    base_time = models.DateTimeField(auto_now=True)
    base_bmail = models.EmailField(max_length=100, blank=True, default='')
    base_web = models.CharField(max_length=200, blank=True, default='')
    base_content = models.TextField(null=False)
    base_response = models.TextField(blank=True, default='')
    
    def __str__(self):
        return self.base_subject