from django.shortcuts import render ,redirect
from django.http import  HttpRequest , HttpResponse 
from .models import Plant

# Create your views here.

def new_add_view(request : HttpRequest):

    if request.method == "POST":
        new_data = Plant(name=request.POST["name"], about=request.POST["about"],used_for=request.POST["used_for"], image=request.FILES["image"],category=request.POST["category"],is_edible= True,created_at = True) 
        new_data.save()
    return render(request,'plant/new_add.html') 


def all_plant_view(request:HttpRequest):
    plants_list = Plant.objects.all()
       
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    if category:
        plants_list = plants_list.filter(category=category)
    
    if is_edible == 'true':
        plants_list = plants_list.filter(is_edible=True)
    elif is_edible == 'false':
        plants_list = plants_list.filter(is_edible=False)

    return render(request, 'plant/all_plant.html', {
        'plants_list': plants_list,
        'category': category,
        'is_edible': is_edible,
    })

def detail_plant_view(request : HttpRequest , plant_id):
    
    detail_plant = Plant.objects.get(pk=plant_id)
    related_plants = Plant.objects.filter(category=detail_plant.category)[0:3]
    
    return render(request , 'plant/detail_plant.html',{'detail_plant':detail_plant , 'related_plants': related_plants} )


def update_plant_view (request : HttpRequest , plant_id ):

    update_plant = Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        update_plant.name = request.POST["name"]
        update_plant.about = request.POST["about"]
        update_plant.used_for = request.POST["used_for"]  
        if "image" in request.FILES:
            update_plant.image = request.FILES["image"]
        
        update_plant.save()
        return redirect("plant:detail_plant_view", plant_id = update_plant.id)
    return render (request , 'plant/update_plant.html', {"update_plant":update_plant})
    

def delete_plant_view (request: HttpRequest,plant_id):

    delete_plant = Plant.objects.get(pk=plant_id)
    delete_plant.delete()
 
    return redirect('main:home_view')


def search_plant_view(request : HttpRequest):

    if 'search' in request.GET and len(request.GET["search"])>=2:        
        search_plant= Plant.objects.filter(name__contains=request.GET["search"])
    else:
        search_plant= []
    return render(request , 'plant/search_plant.html', {"search_plant":search_plant})  