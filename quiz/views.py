from django.shortcuts import render

# Create your views here.

def quiz(request):
    html = 'base.html'
    problems = "4+4"
    context = { 'useMeAbuseMe' : problems }
    return render(request, html, context)


