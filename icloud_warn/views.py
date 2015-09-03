from pyicloud import PyiCloudService
from django.views.generic.edit import BaseFormView
from django import http
from django import forms
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class FindMyPhoneForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
    phone_name = forms.CharField()

class FindMyPhoneView(BaseFormView):
    success_url = "find_my_phone"
    form_class = FindMyPhoneForm

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(FindMyPhoneView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        api = PyiCloudService(form.cleaned_data["email"], form.cleaned_data["password"])
        d = [device for device in api.devices if device["name"] == form.cleaned_data["phone_name"]][0]
        d.play_sound()
        return super().form_valid(form)
