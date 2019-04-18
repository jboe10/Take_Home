from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant
from .forms import ApplicantForm
from django.shortcuts import redirect
# Create your views here.

def applicant_create_view(request):
	amount = request.POST.get('Amount_Required', "")
	age = request.POST.get('Age', "")
	
	form = ApplicantForm(request.POST or None)
	if form.is_valid():
		form.save()
		x = int(amount)
		y = float(age)

		if x>50000 and y<1:
			return redirect('/denied')
		elif x>50000 and y>=1:
			return redirect('/accepted')
		else:
			return redirect('/pending')
	
		form = ApplicantForm()
	context = {
		'form': form
	}
	

	return render(request, "applicant_create.html", context)

def accepted_view(request):
	return render(request,'accepted.html',{})
def denied_view(request):
	return render(request,'denied.html',{})
def pending_view(request):
	return render(request, 'pending.html',{})