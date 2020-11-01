from django.db import models

# Create your models here.
class Host(models.Model):
    ip = models.CharField(max_length=32,default='1.1.1.1')
    hostname = models.CharField(max_length=32,default='unknown')
    def __str__(self):
        return self.hostname

class User(models.Model):
    ip = models.ForeignKey(Host, on_delete=models.CASCADE)
    username = models.CharField(max_length=24,default='myroot')
    password = models.CharField(max_length=24)
    def __str__(self):
        return self.username

        
class Method(models.Model):
    ip = models.ForeignKey(Host, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    command = models.CharField(max_length=1024,default='df -h')
    def __str__(self):
        return self.command

class Record(models.Model):
    begin_time = models.DateTimeField('begin timea',null=True)
    end_time = models.DateTimeField('end time',null=True)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    res = models.IntegerField(default=9999)
    def __str__(self):
        return begin_time
