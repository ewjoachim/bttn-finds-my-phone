from pyicloud import PyiCloudService
from django.views.generic import View
from django import http


class FindMyPhoneView(View):

    def post(self, request):
        api = PyiCloudService(request.POST["email"], request.POST["password"])
        d = [device for device in api.devices if device["name"] == request.POST["phone_name"]][0]
        d.play_sound()
        return http.HttpResponse("OK")
