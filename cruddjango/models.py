from django.db import models


class Member(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.firstname+" "+self.lastname
