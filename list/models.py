from django.db import models

class List(models.Model):
    idList = models.IntegerField(max_length=3)
    toDo = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"{ self.toDo }"
