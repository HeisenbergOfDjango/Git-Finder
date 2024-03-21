from django.shortcuts import render
import requests

def search_users(request):
    location = request.GET.get('location')
    if location:
        url = f"https://api.github.com/search/users?q=location:{location}"
        headers = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            users = response.json().get('items', [])
            return render(request, 'results.html', {'users': users})
        else:
            return render(request, 'error.html', {'error': 'Failed to fetch users.'})
    return render(request, 'search.html')
    