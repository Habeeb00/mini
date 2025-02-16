from django.shortcuts import render
from .models import FoodItemsdb,DailyFoodIntake
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
# Create your views here.



def search_page(request):
    return render(request,"manualtracking/search_results.html")


def select_serving(request):
    return render(request,'manualtracking/select_serve.html')




# backend api

@csrf_exempt
def save_meal(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
           

            meal_type = data.get('mealType')
            food_name = data.get('foodName')
            carbs = data.get('carbs')
            fat = data.get('fat')
            protein = data.get('protein')
            calories = data.get('calories')

            # Add debug prints
            print(f"Meal Type: {meal_type}")
            print(f"Food Name: {food_name}")
            print(f"Carbs: {carbs}, Fat: {fat}, Protein: {protein}, Calories: {calories}")

            DailyFoodIntake.objects.create(
                food_name=food_name,
                meal_type=meal_type,
                date=timezone.now(),
                carbs=carbs,
                fat=fat,
                protein=protein,
                calories=calories
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'fail', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'}, status=400)




def search_item(request):
    query=request.GET.get('q')
    payload=[]
    if query:
        
        results = FoodItemsdb.objects.filter(name__icontains=query.lower())
        
        for result in results:
            payload.append({
                'name' : result.name,
                'GmWt_Desc1':result.GmWt_Desc1,
                'GmWt_1':result.GmWt_1,
                'GmWt_Desc2':result.GmWt_Desc2,
                'GmWt_2':result.GmWt_2,
                'carbohydrate':result.carbohydrate,
                'protien':result.protien,
                'fat':result.fat,
                'energy':result.energy,

            })
           
    return JsonResponse({
            'status':True,
            'payload':payload,
        
        }
    )
    
