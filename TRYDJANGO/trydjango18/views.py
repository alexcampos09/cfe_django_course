from django.shortcuts import render

def about(request):
    return render(request, 'about.html', {})



#Acetemplates!!

def cats(request):
    return render(request, 'cats.html', {})

def pokemon(request):
    return render(request, 'pokemon.html', {})

def sushi(request):
    return render(request, 'sushi.html', {})

def gym(request):
    return render(request, 'gym.html', {})

def tiktak(request):
    return render(request, 'tiktak.html', {})

def todo(request):
    return render(request, 'todo.html', {})

def coffee(request):
    return render(request, 'coffee.html', {})
