from django.shortcuts import render

def show_main(request):
    context = {
        'name': "Baju Tidur",
        'price': '50000',
        'description': 'baju yang nyaman dipakai',
        'category': 'baju',
    }

    return render(request, "main.html", context)