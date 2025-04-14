from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# from django.http import HttpResponse

# Create your views here.

# create view

def create_employee(request):
    if request.method == 'POST':
         form = EmployeeForm(request.POST)

         if form.is_valid():
              form.save()
              return redirect('list')
    else:
         form = EmployeeForm()
    return render(request, 'create.html', {'form':form})

# list view

def employee_list(request):
     employee = Employee.objects.all()
     return render(request, 'list.html', {'employee':employee})
     
# update view
def update_employee(request, pk):
     employee = Employee.objects.get(id=pk)
     if request.method == 'POST':
          form = EmployeeForm(request.POST, instance=employee)

          if form.is_valid():
                form.save()
                return redirect('list')
     else:
          form = EmployeeForm(instance=employee)
     return render(request, 'update.html', {'form':form})

# Delete the employee


def delete_employee(request, pk):
     employee = Employee.objects.get(id=pk)
     if request.method == 'POST':
          employee.delete()
          return redirect('list')
     return redirect('list')