from django.shortcuts import render, get_object_or_404
from student_app.models import Student , Note

# Create your views here.
def index(request):
	students=Student.objects.all().order_by('id')
	return render(request, 'students/index.html', context={ 'students': students})

def details(request,student_id):
	student=Student.objects.get(id=student_id)
	note=Note.objects.filter(student=student)
	print(note)
	return render(request, 'students/details.html', context={ 'student': student ,'note':note})
