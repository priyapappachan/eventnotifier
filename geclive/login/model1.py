
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Addamount(models.Model):
    addamount = models.IntegerField()
    newbalance= models.Account.currentbalance + models.Addamount.addamount
    
    def __unicode__(self):
        return self.accountname
