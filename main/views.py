from django.shortcuts import render

def show_main(request):
    context = {
        'shopName': "Wolverhampton Shop",
        'nama': 'Prasetya Surya Syahputra',
        'kelas': 'PBP E',
    }

    return render(request, "main.html", context)