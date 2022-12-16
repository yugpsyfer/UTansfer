from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    
    def get_username(self):
        return self.user_name
    
    def to_dict(self):
        return {"user_name":self.user_name, "password":self.password, "email":self.email}