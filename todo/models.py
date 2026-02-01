from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskid = models.TextField()
    taskname = models.TextField()


    def __str__(self,request):
        return self.taskname;