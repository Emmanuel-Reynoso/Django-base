from django.shortcuts import render

# New imports
from App.models import Employee
from django.http import HttpResponseRedirect
from django.contrib import messages
# login/logout imports
from django.contrib.auth import authenticate, login, logout # Login / Logout authenticate
from django.contrib.auth.decorators import login_required # Login required
from django.views.decorators.cache import cache_control # Destroy section after logout


# FUNCTION TO RENDER HOME PAGE
@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    employee_list = Employee.objects.all().order_by('-created_at')
    return render(request, "home.html", {"employees":employee_list})

# Function to ADD employee
def add_employee(request):
    if request.method=="POST":
        if request.POST.get('name') \
            and request.POST.get('email') \
            and request.POST.get('occupation') \
            and request.POST.get('salary') \
            and request.POST.get('gender') \
            or request.POST.get('note'):
            employee = Employee()
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.note = request.POST.get('note')
            employee.save()
            messages.success(request, "Employee added successfully!")
            return HttpResponseRedirect("/")
    else:
            return render(request, 'add.html')


# Function to VIEW employee data individually
def employee(request, employee_id):
    employee = Employee.objects.get(id = employee_id)
    if employee != None:
        return render(request, "edit.html", {'employee':employee})

# Function to EDIT employee
def edit_employee(request):
    if request.method == "POST":
        employee = Employee.objects.get(id = request.POST.get('id'))
        if employee != None:
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.note = request.POST.get('note')
            employee.save()
            messages.success(request, "Employee updated successfully!")
            return HttpResponseRedirect("/")

# Function to DELETE employee
def delete_employee(request, employee_id):
    employee = Employee.objects.get(id = employee_id)
    employee.delete()
    messages.success(request, "Employee deleted successfully!")
    return HttpResponseRedirect("/")

# Function to LOGIN
def Login(request):
    if request.user == None or request.user == "" or request.user.username == "":
        return render(request, "login.html")
    else:
        return HttpResponseRedirect('/')

# Login User validate
def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Enter your data correctly.")
            return HttpResponseRedirect('/')

# Function to LOGOUT
def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')
