from django.db import models
from django.urls import reverse
# Create your models here.
class Host(models.Model):
    ip = models.CharField(max_length=32,default='1.1.1.1')
    hostname = models.CharField(max_length=32,default='unknown')
    search_fields = [ 'hostname' ]
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
        return self.username

        
class Method(models.Model):
    ip = models.ForeignKey(Host, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    command = models.CharField(max_length=512,default='df -h')
    comments = models.CharField(max_length=512,default='comments has not been added')
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
    methods = models.ManyToManyField(Method, through='FlowMethodMembership')
    name = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name+"::"+self.create_time.strftime('%Y-%m-%d %H:%M:%S')
    class Meta:
        ordering = [ 'create_time' ]
    def get_absolute_url(self):
        return reverse('flowdetail', args=[str(self.id)])

class FlowMethodMembership(models.Model):
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    flow = models.ForeignKey(Flow, on_delete=models.CASCADE)
    rank = models.IntegerField(default=-1)
    status = models.IntegerField(default=-1)
    add_time = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['method','rank']
