from django.db import models

# Create your models here.

class Task(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item