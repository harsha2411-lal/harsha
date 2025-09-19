from django.shortcuts import render

def home(request):
    message = ''
    show_video = False
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        if name == 'lalitha' and date == '2025-09-11':
            show_video = True
        else:
            message = 'You entered wrong data.'
    return render(request, 'home.html', {'show_video': show_video, 'message': message})
