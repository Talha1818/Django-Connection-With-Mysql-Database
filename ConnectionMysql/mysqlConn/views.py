from django.shortcuts import render, HttpResponse
from .models import Employee
# Create your views here.
def index(request):
    emp = Employee.objects.all()
    details = []
    for i in emp:
        name = i.name
        email = i.email
        address = i.address
        details.append((name,email, address))
    return HttpResponse(f"{details}")
    # e = Employee(name='faisal', email='ta@gmail.com', address='Okay great!')
    # e.save()

    # print(emp.get('name'))
