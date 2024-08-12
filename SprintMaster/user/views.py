from user.models import CustomUser
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# @csrf_exempt 
# def signup(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '').strip()
#         email = request.POST.get('email', '').strip()
#         password1 = request.POST.get('password1', '').strip()
#         password2 = request.POST.get('password2', '').strip()
#         role = request.POST.get('role', '').strip()

#         if name and email and password1 and password2:
#             if password1 != password2:
#                 return render(request, 'user/signup.html', {'error': "Passwords do not match"})

#             try:
#                 user = CustomUser.objects.create_user(
#                     username=name, email=email, password=password1, role=role)
#                 user.save()
#                 return redirect('/login/')
#             except IntegrityError as e:
#                 if 'UNIQUE constraint failed' in str(e):
#                     if 'user_customuser.username' in str(e):
#                         error_message = 'Username already exists'
#                     elif 'user_customuser.email' in str(e):
#                         error_message = 'Email already exists'
#                     else:
#                         error_message = 'Error creating user. Please try again.'
#                 else:
#                     error_message = 'Error creating user. Please try again.'
#                 return render(request, 'user/signup.html', {'error': error_message})
#             except Exception as e:
#                 return render(request, 'user/signup.html', {'error': "Error creating user. Please try again."})
#         else:
#             return render(request, 'user/signup.html', {'error': "All fields are required."})
#     else:
#         return render(request, 'user/signup.html')
@csrf_exempt  # For testing only; remove in production
def signup(request):
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': "Invalid JSON format"}, status=400)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        password1 = data.get('password1', '').strip()
        password2 = data.get('password2', '').strip()
        role = data.get('role', '').strip()

        if name and email and password1 and password2:
            isPasswordMatched(password1, password2 )
            try:
                user = CustomUser.objects.create_user(
                    username=name, email=email, password=password1, role=role)
                user.save()
                return JsonResponse({'success': True, 'redirect_url': '/login/'}, status=201)
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    if 'user_customuser.username' in str(e):
                        error_message = 'Username already exists'
                    elif 'user_customuser.email' in str(e):
                        error_message = 'Email already exists'
                    else:
                        error_message = 'Error creating user. Please try again.'
                else:
                    error_message = 'Error creating user. Please try again.'
                return JsonResponse({'error': error_message}, status=400)
            except Exception as e:
                return JsonResponse({'error': "Error creating user. Please try again."}, status=400)
        else:
            return JsonResponse({'error': "All fields are required."}, status=400)
    else:
        return JsonResponse({'error': "Invalid request method"}, status=405)


def login_views(request):
    return render(request, 'user/login.html')


def isPasswordMatched(password, repeatedPassword):
    if password != repeatedPassword:
        return JsonResponse({'error': "Passwords do not match"}, status=400)
