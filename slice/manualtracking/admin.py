from django.contrib import admin
from . models import FoodItemsdb,DailyFoodIntake


class DisplayFoodItemsDb(admin.ModelAdmin):
    list_display=('id','name','energy','protien','carbohydrate','fat','GmWt_1','GmWt_Desc1','GmWt_2','GmWt_Desc2')
    
class DisplayDailyFoodIntake(admin.ModelAdmin):
    list_display=('id','food_name','meal_type','date','carbs','fat','protein','calories')

# Register your models here.
admin.site.register(FoodItemsdb,DisplayFoodItemsDb)
admin.site.register(DailyFoodIntake,DisplayDailyFoodIntake)