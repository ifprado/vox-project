from django.shortcuts import render

# Create your views here.

def indexJordan(request):
    html = 'jordanTest.html'
    problems = "4+4"
    context = { 'useMeAbuseMe' : problems }
    return render(request, html, context)