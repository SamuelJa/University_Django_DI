from django.db import models

# Create your models here.

class Student(models.Model):
	prenom=models.CharField(max_length=20)
	nom=models.CharField(max_length=20)
	date=models.DateField()

	def __str__(self):
		return self.prenom

class Note(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	matiere=models.CharField(max_length=20)
	note=models.IntegerField(default=0)
	coefficient=models.IntegerField(default=0)

	def __str__(self):
		return self.matiere
