import json
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def main(request):
    # Fetch existing user data
    try:
        response = requests.get('http://127.0.0.1:5000/api/get')
        if response.status_code == 200:
            data = response.json()['data']
        else:
            data = []
    except requests.exceptions.RequestException as e:
        data = []
        print(f'Error fetching data: {str(e)}')

    return render(request, 'form.html', {'data': data})

def insert(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        category = request.POST.get('category')
        
        user_data = {
            'user_id': user_id,
            'name': name,
            'email': email,
            'category': category
        }
        
        try:
            insert_data = requests.post('http://127.0.0.1:5000/api/data', json=user_data)
            if insert_data.status_code == 200:
                # Return the inserted user data as JSON
                return JsonResponse(user_data)
            else:
                return HttpResponse('Failed to send data to Flask API', status=insert_data.status_code)
        except requests.exceptions.RequestException as e:
            return HttpResponse(f'Error sending data to Flask API: {str(e)}', status=500)
    
    return HttpResponse('Invalid request method', status=400)

def update(request):
    if request.method == 'POST':
        user_id2 = request.POST.get('user_id2') 
        new_category = request.POST.get('new_category')

        updated_user_data = {
            'new_category': new_category,
            'user_id2': user_id2,
        }
        
        try:
            update_response = requests.post('http://127.0.0.1:5000/api/newdata', json=updated_user_data)
            if update_response.status_code == 200:
                # Return the updated data as JSON
                return JsonResponse(updated_user_data)
            else:
                return HttpResponse('Failed to send data to Flask API', status=update_response.status_code)
        except requests.exceptions.RequestException as e:
            return HttpResponse(f'Error sending data to Flask API: {str(e)}', status=500)

    return HttpResponse('Invalid request method', status=400)
