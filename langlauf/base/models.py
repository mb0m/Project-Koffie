from django.db import models
from django.contrib.auth.models import User


class Koffieboon(models.Model):
    name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100, blank=True, default='')
    harvest_season = models.CharField(max_length=100, blank=True, default='')
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Tasting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bean = models.ForeignKey(Koffieboon, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} – {self.bean.name}"


class Profile(models.Model):
      BREW_METHODS = [
          ('espresso', 'Espresso'),
          ('filter', 'Filter'),
          ('french_press', 'French Press'),
          ('pour_over', 'Pour Over'),
          ('aeropress', 'AeroPress'),
          ('moka_pot', 'Moka Pot'),
      ]

      user = models.OneToOneField(User, on_delete=models.CASCADE)
      city = models.CharField(max_length=100, blank=True, default='')
      date_of_birth = models.DateField(null=True, blank=True)
      favorite_method = models.CharField(max_length=50, choices=BREW_METHODS, blank=True, default='')

      def __str__(self):
          return f"{self.user.username} – profiel"
# Create your models here.