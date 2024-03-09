# views.py
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# views.py

from django.shortcuts import render, redirect
from .forms import UserDataForm

# views.py

from django.shortcuts import render, redirect
from .forms import UserDataForm

from django.shortcuts import render

def success_view(request):
    return render(request, 'success.html')
def previous(request):
    return render(request, 'previous.html')
def mini(request):
    return render(request, 'mini.html')


from django.shortcuts import render, redirect
from .forms import UserDataForm  # Import your form
from .models import UserData  # Import your model

import razorpay
from django.conf import settings
from django.http import JsonResponse


# views.py

from django.shortcuts import redirect

def submit_data(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            try:
                # Save the form data to the database
                new_data = UserData.objects.create(
                    name=form.cleaned_data['name'],
                    profession=form.cleaned_data['profession'],
                    email=form.cleaned_data['email'],
                    phone_number=form.cleaned_data['phone_number'],
                )
                request.session['option_selected'] = new_data.option_selected
                return redirect('success')  # This will trigger the success_view
            except Exception as e:
                print(str(e))
                return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)
    else:
        form = UserDataForm()
    return render(request, 'service.html', {'form': form})



def home(request):
    return render(request, 'index.html')

from django.shortcuts import render

def service1_view(request):
    return render(request, 'service.html')

def service2_view(request):
    return render(request, 'service.html')

def AKTU_ONE_SHOT(request):
    return render(request, 'update.html')

from django.shortcuts import redirect
from django.urls import reverse

def payment_success(request):
    # Assuming you have a session variable or some way to determine the selected option
    # You can retrieve the selected option from the session or any other method you are using
    option_selected = request.session.get('option_selected', None)
    print(option_selected)
    if option_selected:
        return redirect(reverse('download_zip', kwargs={'option_selected': option_selected}))
    else:
        # Handle the case where the option is not selected
        return redirect('home')
import os
from django.http import HttpResponse, FileResponse
from django.conf import settings
import os

def download_zip(request, option_selected):
    # Determine the zip file name based on the option selected
    if option_selected == 1:
        zip_file_name = 'goodweb.zip'
    elif option_selected == 2:
        zip_file_name = 'zipfile2.zip'
    else:
        return HttpResponse("Invalid option selected", status=400)

    # Construct the full path to the zip file
    zip_file_path = 'zipfiles\goodweb.zip'

    # Check if the file exists
    if os.path.exists(zip_file_path):
        try:
            # Open the zip file and serve it as a response
            with open(zip_file_path, 'rb') as zip_file:
                response = FileResponse(zip_file)
                response['Content-Disposition'] = f'attachment; filename="{zip_file_name}"'
                return response
        except Exception as e:
            return HttpResponse(f"Error reading the file: {e}", status=500)
    else:
        # Handle the case where the zip file does not exist
        return HttpResponse("File not found", status=404)

