from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("hi")

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