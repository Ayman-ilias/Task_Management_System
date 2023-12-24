from django.db import models
from TaskCatagory.models import TaskCatagory

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    catagory = models.ManyToManyField(TaskCatagory)

    def __str__(self):
        return self.taskTitle

