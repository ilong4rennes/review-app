from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    users = models.ManyToManyField(to=User, blank=True, through='Review')
    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_STARS = [
        (1, 'One Star'),
        (2, 'Two Star'),
        (3, 'Three Star'),
        (4, 'Four Star'),
        (5, 'Five Star'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_STARS)
    def __str__(self):
        return "{} rates {} at {} star.".format(str(self.user), str(self.business), str(self.rating))