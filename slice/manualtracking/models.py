from django.db import models
from django.conf import settings
from django.utils import timezone 
# Create your models here.


#database containing food items
class FoodItemsdb(models.Model):
    name=models.CharField(max_length=100)
    energy=models.IntegerField()
    protien=models.DecimalField(max_digits=10,decimal_places=5)
    carbohydrate=models.DecimalField(max_digits=10,decimal_places=5)
    fat=models.DecimalField(max_digits=10,decimal_places=5)
    GmWt_1=models.DecimalField(max_digits=10,decimal_places=5,null=True)
    GmWt_Desc1=models.CharField(max_length=100,null=True)
    GmWt_2=models.DecimalField(max_digits=10,decimal_places=5,null=True)
    GmWt_Desc2=models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name_plural="FoodItemsFinal"

    def __str__(self):
        return self.name

    
#database storing daily food intake 
class DailyFoodIntake(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_name=models.CharField(max_length=100)
    meal_type = models.CharField(max_length=50) 
    date = models.DateTimeField(default=timezone.now)
    carbs = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return self.food_name

