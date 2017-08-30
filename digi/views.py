from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View

from .forms import StudentForm,ProfessorForm,StudentLoginForm,ProfessorLoginForm,UserForm

def page1(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'digi/login_page_wt_project/teacher_or_student.html')

def page2(request):
	if request.method == 'POST': # If the form has been submitted...
		#form = ContactForm(request.POST) # A form bound to the POST data
		#if abc01.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			# ...
			pro1= request.POST['profession']
			#print (pro1)
			if pro1=="Teacher":
				form = ProfessorLoginForm()
				return render(request, 'digi/page24.html',{'form':form})
			else:
				form = StudentLoginForm()
				return render(request, 'digi/page23.html',{'form':form})


#def page3(request):#Student registration form display funtion
	# if request.method == 'POST':
	# 	form  = StudentForm(request.POST)
	# 	if form.is_valid:
	# 		obj = Student()
	# 		obj.name = form.cleaned_data['student_name']
	# 		obj.save()
	#form = StudentForm()
#	return render(request, 'digi/page3.html',{'form':form})


#def page4(request):#Function to display the registration page of professor
#	form=ProfessorForm()
#	return render(request,'digi/page4.html',{'form':form})

# def page23(request):
# 	return render(request, 'gad1/page5.html')

#def page5(request):# first 5 lines are for saving the data into db
	#if request.POST :
	#	form = ProfessorForm(request.POST)
	#	if form.is_valid():
	#		prof = form.save()
	#return render(request, 'digi/2018_notebook/teacher_display.html')





#def page6(request):# first five lines are for saving the data into the db
	#if request.POST :
	#	form = StudentForm(request.POST)
	#	if form.is_valid():
	#		prof = form.save()
	#return render(request, 'digi/page6.html')

class UserFormView(View):#for saving and processing professor data
	form_class=UserForm
	template_name='digi/login_page_wt_project/Teacher_register.html'

    #display blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#process form data
	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user=form.save(commit=False)

			# cleaned (normalised) data
			username = form.cleaned_data('name')
			gender = form.cleaned_data('gender')
			mobileno = form.cleaned_data('mobileno')
			dept = form.cleaned_data('dept')
			sap = form.cleaned_data('sap')
			email = form.cleaned_data('email')
			password=form.cleaned_data('password')
			user.set_password(password)
			user.set_username(username)
			user.save()

			# returns user object if credentials are correct
			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active():
					login(request,user)
					return redirect('digi/login_page_wt_project/prof_core.html')
		return render(request, self.template_name, {'form': form})


def index(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'digi/page1.html')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

# def handle_uploaded_file(f):
#     with open('C:/gargee_june/form1a.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)