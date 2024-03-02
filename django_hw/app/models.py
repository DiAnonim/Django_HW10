from django.db import models

class Todo(models.Model):
    class TodoStatus(models.TextChoices):
        COMPLETED = "C", "completed"
        IN_PROCESS = "P", "in process"
        DONE = "D", "Done"

    title = models.CharField(max_length = 255)
    description = models.TextField()
    status = models.CharField(max_length = 255, choices = TodoStatus.choices, default = TodoStatus.COMPLETED)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
