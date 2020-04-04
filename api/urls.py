from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.company_list),
    path('companies/<int:pk>/', views.companies_detail),
    path('companies/<int:pk>/vacancies/', views.company_vacancies),
    path('vacancies/',views.vacancy_list),
    path('vacancies/<int:pk>/', views.vacancies_detail),
    path('vacancies/top_ten/',views.top_ten)
]
# /api/ - List of all Companies
# /api/companies/<int:id>/ - Get one Company
# /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# /api/vacancies/ - List of all Vacancies
# /api/vacancies/<int:id>/ - Get one Vacancy
# /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary
