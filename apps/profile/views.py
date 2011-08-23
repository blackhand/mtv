from profile.forms import *
from registration.views import *
from ubigeo.views import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def register(request):
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            ##Profile.objects.get(user = User.objects.get(pk=request.POST["user"]),first_name = request.POST["first_name"],last_name = request.POST["last_name"], email = request.POST["email"], birth_date = request.POST["birth_date"], ubigeo = Ubigeo.objects.get(pk=request.POST["user"]), address = request.POST["address"], home_phone = request.POST["home_phone"], mobile_phone = request.POST["mobile_phone"], document_code = request.POST["document_code"]).save()
            profile_form.save()
            return HttpResponseRedirect('/accounts/register/')
    return render_to_response('registration/registration_form.html',
                              {'form': profile_form},
                              context_instance=context)
