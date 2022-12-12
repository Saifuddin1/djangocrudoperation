from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Student
from .forms import StudentForm
# Create your views here.


# view to add and show the data of a student
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            stu = Student(name = name, email = email, password = password)
            stu.save()
            form = StudentForm()
    else:
        form = StudentForm()
    students = Student.objects.all()
    return render(request, "my_app/addandshow.html", {"form":form, "students":students})


# view to update the data of a student
def update_student(request, id):
    if request.method == 'POST':
        pi = Student.objects.filter(pk = id).first()
        form = StudentForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = Student.objects.filter(pk = id).first()
        form = StudentForm(instance = pi)
    return render(request, "my_app/updatestudent.html", {"form":form})


# view to delete the data of a student
def delete_student(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk = id)
        student.delete()
        return HttpResponseRedirect("/student/add_student")
