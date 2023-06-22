from django.shortcuts import render, HttpResponse
from .models import Vacancy, Company
# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse("Найдите работу или работника мечты")

def contacts(request):
    return HttpResponse('''
    <div>
    Phone: +996777123456 <br>
    Email: office@handhunter.kg"
    </div>
    ''')

def address(request):
    return HttpResponse('''
    <ol>
    <li>Kievskaya-Sovetskaya</li>
    <li>Kurmanzhan-Datka-164</li>
    </ol>
    ''')

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies':vacancies}
    return render(request, 'vacancies.html', context)

def company_list(request):
    companies = Company.objects.all()
    context = {'companies':companies}
    return render(request, 'companies.html', context)

