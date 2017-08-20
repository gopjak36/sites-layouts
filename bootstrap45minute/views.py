from django.shortcuts import render

def Bootstrap45minuteHome(request):
    ''' Home Page method '''

    return render(request, 'bootstrap45minute/homepage.html', {})
