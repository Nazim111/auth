import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from users.forms import UserCreationForm

KEY = '*'
LINK_1 = 'http://136.244.93.168/admin_api/v1/clicks/log'
headers = {'Api-Key': f"{KEY}", 'accept': 'application/json'}


def index(request):
    a = {
        "limit": 2,
        "offset": 0,
        # "filters": [
        #   {
        #     "name": "ID",
        #     "operator": "bogdan",
        #   }
        # ],
    }

    r = requests.post(LINK_1, headers=headers, data=a)
    print(r.json())
    clicks_dict = r.json()
    total = clicks_dict.get('total')
    print(total)

    data = {"clicks": f"{total}"}
    return render(request, "stat.html", context=data)

# class Register(View):
#     template_name = 'registration/register.html'
#
#     def get(self, request):
#         context = {
#             'form': UserCreationForm()
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#         context = {
#             'form': form
#         }
#         return render(request, self.template_name, context)
