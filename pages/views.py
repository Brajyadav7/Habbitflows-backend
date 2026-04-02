from django.shortcuts import render

def welcome(request): return render(request, 'pages/welcome.html')
def about(request):   return render(request, 'pages/about.html')
def contact(request): return render(request, 'pages/contact.html')
def privacy(request): return render(request, 'pages/privacy.html')
def terms(request):   return render(request, 'pages/terms.html')
def blog_list(request): return render(request, 'pages/blog_list.html')
def blog1(request):   return render(request, 'pages/blog1.html')
def blog2(request):   return render(request, 'pages/blog2.html')
def blog3(request):   return render(request, 'pages/blog3.html')
def blog4(request):   return render(request, 'pages/blog4.html')
def blog5(request):   return render(request, 'pages/blog5.html')
