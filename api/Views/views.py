from django.http import JsonResponse
from rest_framework.response import Response
from api.models import Company,Vacancy
from rest_framework.views import APIView
from rest_framework import status

from api.models import Vacancy
from api.serializers import VacancySerializer
def company_list(request):
    companies = Company.objects.all()
    json_companies = [c.to_json() for c in companies]
    return JsonResponse(json_companies, safe=False)
# def vacancy_list(request):
#     vacancies = Vacancy.objects.all()
#     json_vacancies = [c.to_json() for c in vacancies]
#     return JsonResponse(json_vacancies, safe=False)

# def companies_detail(request, pk):
#     try:
#         company = Company.objects.get(id=pk)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#
#     return JsonResponse(company.to_json())
#
# def vacancies_detail(request, pk):
#     try:
#         vacancy = Vacancy.objects.get(id=pk)
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#
#     return JsonResponse(vacancy.to_json())
#
#
# def company_vacancies(request, pk):
#     try:
#         company = Company.objects.get(id=pk)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#
#     vacancies = company.vacancy_set.all()
#     json_vacancies = [p.to_json() for p in vacancies]
#     return JsonResponse(json_vacancies, safe=False)
#
# def top_ten(request):
#     vacancies = Vacancy.objects.all().values("name", "company__name").order_by("-salary")[:10]
#     json_vacancies = [v.to_json() for v in vacancies]
#     return JsonResponse(json_vacancies, safe=False)

class VacancyView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VacancyDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        vacancy.delete()

        return Response({'deleted': True})