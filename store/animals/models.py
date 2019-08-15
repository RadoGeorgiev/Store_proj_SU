from django.db import models

# Create your models here.


class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Animal(models.Model):
    KIND_CHOISES = (
        ('D', 'Dog'),
        ('C', 'Cat')
    )

    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField()
    kind = models.CharField(max_length=1, choices=KIND_CHOISES)
    # owner = models.ForeignKey(Owner, on_delete=None, default=0)

    def __str__(self):
        return f'My name is {self.name} and I am {self.breed}'


