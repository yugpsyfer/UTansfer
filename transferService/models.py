from django.db import models

# Create your models here.

class Data(models.Model):
    pass

class UploadFile(models.Model):
    file = models.FileField()
    file_url = models.URLField()

    def get_username(self):
        return self.user_name

    def to_dict(self):
        return {"file_url": self.file_url}