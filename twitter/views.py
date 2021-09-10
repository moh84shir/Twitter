from django.shortcuts import render


def left_menu(request):
    context = {
        "user": request.user
    }
    return render(request, 'shared/LeftMenu.html', context)