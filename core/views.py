from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'name': 'Company 1',
        'nums': [i for i in range(5)],
        'is_logged_in': False,
        'vacancy': {
            'id': 1,
            'name': 'Vacancy 1'
        },
        'vacancies': [{
            'id': i,
            'name': 'Company {}'.format(i)
        } for i in range(5)]
    }
    return render(request,context)


def show_vacancy(request, pk):
    return HttpResponse('<h1>{}</h1>'.format(pk))

