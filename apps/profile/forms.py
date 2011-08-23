"""
Forms and validation code for user profile.

"""
from django import forms
from profile.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

    def save(self,force_insert=False, force_update=False, commit=True):
        user = User.objects.get(pk=self.user)
        profile = Profile.objects.create(user=user,first_name = self.instance.first_name,last_name = self.instance.last_name,email = self.instance.email,birth_date = self.instance.birth_date,ubigeo = Ubigeo.objects.get(pk=self.instance.ubigeo),address = self.instance.address,home_phone = self.instance.home_phone,mobile_phone = self.instance.mobile_phone,document_code=self.instance.document_code)
        self.save()
