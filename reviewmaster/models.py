from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

    def rated_businesses(self):
        return self.business_set.all()

    # Content-based recommendation
    def content_based_recommended_businesses(self):
        # item profile
        rated_businesses = self.review_set.all().values_list('business', flat=True)

        # user profile
        rated_business_cities = Business.objects.filter(pk__in=rated_businesses).values_list('city', flat=True)

        # match
        recommended_businesses = Business.objects.filter(city__in=rated_business_cities).exclude(pk__in=rated_businesses)
        return recommended_businesses

    def collaborative_based_recommended_businesses(self):
        rated_businesses = self.review_set.all().values_list('business', flat=True)
        similar_users = User.objects.exclude(pk=self.pk).filter(
            review__business__in=rated_businesses
        ).distinct()
        similar_businesses = Business.objects.filter(review__user__in=similar_users)
        recommended_businesses = similar_businesses.exclude(review__user=self)
        return recommended_businesses

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