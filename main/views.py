from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Jersey FC Barcelona X Travis Scott (Official)',
        'price': '1200000',
        'description': 'Jersey Barcelona yang berkolaborasi dengan Travis Scott',
        'thumbnail': 'https://share.google/be6yjHPUv0jePt1yr',
        'category': 'Jersey',
        'is_featured': 'Yes',
    }

    return render(request, "main.html", context)