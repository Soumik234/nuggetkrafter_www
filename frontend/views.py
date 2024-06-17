from django.shortcuts import render, redirect

def landing_page(request):
	return render(request, 'index.html')

def contact_us(request):
	return render(request, 'contact.html')

def about_us(request):
	return render(request, 'about.html')

def login_redirect(request):
    return redirect('https://cmp.nuggetkrafter.com/')

def solutions(request):
	return render(request, 'solutions.html')