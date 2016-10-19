from django.shortcuts import render
from django.conf import settings
import requests

url = "https://{0}.monitoringclient.com/v2.2/computers?api_key={1}&expand[]=plugin_results".format(settings.WATCHMAN_SUBDOMAIN, settings.WATCHMAN_API)
r = requests.get(url)
computers = r.json()

def get_computer_id(request):
    for computer in computers:
        return computer['id']

def get_computer_list(request):
    if r.status_code == requests.codes.ok:
        context = {
            'computers':computers,
        }
        return render(request, 'computers/list.html', context)
    else:
        print('Cannot retrieve computers.')

def get_computer_detail(request, get_computer_id):
    for computer in computers:
        context = {
            'computer':computer,
        }
        return render(request, 'computers/detail.html', context)
