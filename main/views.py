from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'GoalMate',
        'student_name': 'Rayyan Emir Muhammad',
        'student_class': 'PBP B', 
    }

    return render(request, "main.html", context)