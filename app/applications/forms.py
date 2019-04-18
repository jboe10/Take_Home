from django import forms

from .models import Applicant


class ApplicantForm(forms.ModelForm):

	class Meta:
		model = Applicant
		fields = ['Name','Amount_Required','Buisness_Type','Age', ]

	def clean_Amount_Required(self, *args, **kwargs):
		Amount = self.cleaned_data.get("Amount_Required")
		if isinstance(Amount,int) and Amount>0:
			return Amount
		else:
			raise forms.ValidationError("Please enter a positive whole number") 

	def clean_Age(self, *args, **kwargs):
		age = self.cleaned_data.get("Age")
		if age>0:
			return age
		else:
			raise forms.ValidationError("Please enter a positive number")
