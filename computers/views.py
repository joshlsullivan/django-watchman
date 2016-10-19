from django.shortcuts import render
from django.conf import settings
import requests

url = "https://{0}.monitoringclient.com/v2.2/computers?api_key={1}&expand[]=plugin_results".format(settings.WATCHMAN_SUBDOMAIN, settings.WATCHMAN_API)

def get_computer_list(request):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        computers = r.json()
        context = {
            'computers':computers,
        }
        return render(request, 'computers/list.html', context)
    else:
        print('Cannot retrieve computers.')
