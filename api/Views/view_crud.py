import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Vacancy


# CRUD - For Category Model

@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [c.to_json() for c in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)

        # option 1
        # category = Category(name=data['name'])
        # category.save()

        # option 2
        vacancy = Vacancy.objects.create(name=data.get('name'))

        return JsonResponse(vacancy.to_json())


@csrf_exempt
def vacancy_detail(request, category_id):
    try:
        vacancy = Vacancy.objects.get(id=category_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    # Get one objects
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())

    # Update selected objects
    elif request.method == 'PUT':
        data = json.loads(request.body)

        vacancy.name = data.get('name', vacancy.name)
        vacancy.save()

        return JsonResponse(vacancy.to_json())

    # Delete selected object
    elif request.method == 'DELETE':
        vacancy.delete()

        return JsonResponse({'deleted': True})