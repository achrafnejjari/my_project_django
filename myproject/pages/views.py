from django.shortcuts import render

def index(request):
    x = {'name': 'ahmed', 'age': 18}
    return render(request, 'pages_html/index.html', {'x': x})  # Make sure 'x' is passed as a dictionary
