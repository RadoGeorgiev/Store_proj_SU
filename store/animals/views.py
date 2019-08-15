from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Animal
from django.core.serializers import serialize

# Create your views here.


def create_animal(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    breed = request.GET.get('breed')
    kind = request.GET.get('kind')
    image_url = request.GET.get('image_url')
    description = request.GET.get('description')

    animal = Animal(name=name, age=age, breed=breed, kind=kind, image_url=image_url, description=description)

    animal.save()
    return HttpResponse('Created')

    # http://127.0.0.1:8000/animals/create/?name='Novo'&age='1'&breed='some breed'&description=''&kind='D'&image_url='https://i.kinja-img.com/gawker-media/image/upload/s--HqfzgkTd--/c_scale,f_auto,fl_progressive,q_80,w_800/wp2qinp6fu0d8guhex9v.jpg'
    # url is always string so ' ' is not needed !!!


def edit_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    name = request.GET.get('name')
    animal.name = name
    return HttpResponse('Name Edited')


def delete_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    animal.delete()

    # shorter version to delete the instance
    # Animal.objects.get(pk=animal_id).delete()

    return HttpResponse(f'deleted {animal_id}')


def serialized_data(data):
    try:
        return serialize('json', data)
    except Exception as exe:
        return serialize('json', [data])


def get_all_animals(request):
    name = request.GET.get('name')
    if name:
        animal = Animal.objects.all().filter(name=name)
        return HttpResponse(serialized_data(animal))
    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))


def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


def get_all_dogs(request):
    dogs = Animal.objects.filter(age=12, kind='D')
    return HttpResponse(serialized_data(dogs))


def order_animals(request):
    animals = Animal.objects.all().order_by('-age', 'name')
    return HttpResponse(serialized_data(animals))