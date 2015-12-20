import json
from pyicloud import PyiCloudService, exceptions
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
    success_url = "./"
    form_class = FindMyPhoneForm

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(FindMyPhoneView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        try:
            try:
                api = PyiCloudService(form.cleaned_data["email"], form.cleaned_data["password"])
            except exceptions.PyiCloudFailedLoginException:
                raise forms.ValidationError("Invalid email or password.")

            devices = [device for device in api.devices if device["name"] == form.cleaned_data["phone_name"]]
            try:
                device = devices[0]
            except IndexError:
                raise forms.ValidationError({"phone_name": "Device {} not found".format(form.cleaned_data["phone_name"])})

        except forms.ValidationError as exc:
            form.add_error(None, exc)
            return self.render_to_response({"form": form})

        else:
            device.play_sound()
            return super().form_valid(form)

    def render_to_response(self, context):
        if "form" in context and context["form"].is_bound and not context["form"].is_valid():
            return http.HttpResponseBadRequest(json.dumps(context["form"].errors))
        return http.HttpResponse("OK")
