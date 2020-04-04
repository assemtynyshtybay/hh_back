from django.http import JsonResponse
from api.models import Company,Vacancy


def company_list(request):
    companies = Company.objects.all()
    json_companies = [c.to_json() for c in companies]
    return JsonResponse(json_companies, safe=False)
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    json_vacancies = [c.to_json() for c in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def companies_detail(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(company.to_json())

def vacancies_detail(request, pk):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(vacancy.to_json())


def company_vacancies(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    vacancies = company.vacancy_set.all()
    json_vacancies = [p.to_json() for p in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def top_ten(request):
    vacancies = Vacancy.objects.all().values("name", "company__name").order_by("-salary")[:10]
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)