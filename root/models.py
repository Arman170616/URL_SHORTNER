from django.db import models
from hashlib import md5

class Url(models.Model):
    full_url = models.CharField(max_length=400, unique=True)
    short_url = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.short_url
    
    @classmethod
    def create(self,full_url):
        temp_url = md5(full_url.encode()).hexdigest()[:5]    # hashlib.md5(str2hash.encode())
        try :
            obj = self.objects.create(full_url = full_url, short_url=temp_url)
        except:
            obj = self.objects.get(full_url = full_url)
        return obj 