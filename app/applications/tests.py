from django.test import TestCase
from .models import Applicant
from .views import *
import re
test_applicant_1 = {'Name':'Experian',
			'Amount_Required':100000,
			'Buisness_Type':'MS',
			'Age':1,
		}
# Create your tests here.
class ApplicationViewTest(TestCase):

	def test_applicant_create_view(self):
		test_applicant_1 = {'Name':'Experian',
			'Amount_Required':100000,
			'Buisness_Type':'MS',
			'Age':2,
		}
		test_applicant_2 = {'Name':'Experian',
			'Amount_Required':100000,
			'Buisness_Type':'MS',
			'Age':.5,
		}
		test_applicant_3 = {'Name':'Experian',
			'Amount_Required':100,
			'Buisness_Type':'MS',
			'Age':1,
		}

		response = self.client.post('/',test_applicant_1,follow=True)
		self.assertRedirects(response,'/accepted/')

		response = self.client.post('/',test_applicant_2,follow=True)
		self.assertRedirects(response,'/denied/')

		response = self.client.post('/',test_applicant_3,follow=True)
		self.assertRedirects(response,'/pending/')

