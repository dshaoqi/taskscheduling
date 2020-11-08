from django.db import models
from django.urls import reverse
# Create your models here.
class Host(models.Model):
    ip = models.CharField(max_length=32,default='1.1.1.1')
    hostname = models.CharField(max_length=32,default='unknown')
    def get_absolute_url(self):
        return reverse('hostdetail',args=[str(self.id)])
    def __str__(self):
        return self.ip
    def display_users(self):
        return ','.join([user.username for user in self.user_set.all()[:3]])
    display_users.short_description = 'Users'

class User(models.Model):
    ip = models.ForeignKey(Host, on_delete=models.CASCADE)
    username = models.CharField(max_length=24,default='myroot')
    password = models.CharField(max_length=24)
    def __str__(self):
        return self.ip.ip+"::"+self.username

        
class Method(models.Model):
    ip = models.ForeignKey(Host, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    command = models.CharField(max_length=1024,default='df -h')
    create_time = models.DateTimeField(auto_now=True)
    expect_res = models.IntegerField(default=4398)
    def __str__(self):
        return self.ip.ip+"::"+self.username.username+"::"+self.command

class Record(models.Model):
    begin_time = models.DateTimeField('begin time',null=True)
    end_time = models.DateTimeField('end time',null=True)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    res = models.IntegerField(default=4399)
    class Meta:
        ordering = [ 'begin_time' ]
    def __str__(self):
        return self.begin_time.strftime('%Y-%m-%d %H:%M:%S')+"::"+self.method+"::"+str(res)

class Flow(models.Model):
    method = models.ManyToManyField(Method)
    name = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name+"::"+self.create_time.strftime('%Y-%m-%d %H:%M:%S')
