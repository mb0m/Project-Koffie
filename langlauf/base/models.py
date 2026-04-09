from django.db import models
from django.contrib.auth.models import User

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
      city = models.CharField(max_length=100)
      date_of_birth = models.DateField()
      favorite_method = models.CharField(max_length=50, choices=BREW_METHODS)

      def __str__(self):
          return f"{self.user.username} – profiel"
# Create your models here.