from django.shortcuts import render

# Create your views here.

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})


def page_not_found(request, exception):
    """
    500 Page not found
    """
    return render(request, 'common/500.html', {})
