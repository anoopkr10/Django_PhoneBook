from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNo = models.IntegerField()

    def __str__(self):
        return self.name + ',' + self.email + ',' + str(self.phoneNo)

    class Meta:
        db_table = "Contacts"
