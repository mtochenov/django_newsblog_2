from django.shortcuts import redirect


def get_start_page(request):
    """redirect to start page"""
    return redirect('news/')
