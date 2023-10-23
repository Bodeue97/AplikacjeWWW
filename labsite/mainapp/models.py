from django.db import models

MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        
    )

class ObjectToRemigrate(models.Model):
    name = models.CharField(max_length=10)


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.CharField(max_length = 1, choices = GENDERS, default="M")

    def __str__(self):
        return self.name

class ModelForAdmin(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()

    def __str__(self):
        return self.name