from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Accesskey(models.Model):
    status_choices={
        'ACTIVE':'active',
       'EXPIRED':'expired',
       'REVOKED':'revoked'
    }
    key=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,choices=status_choices)
    date_procured=models.DateTimeField(auto_now_add=True)
    expiry_date=models.DateField()
    
    def __str__(self):
        return f'{str(self.key)} for {self.user.username}'