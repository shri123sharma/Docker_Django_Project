from django.http import HttpResponseRedirect
from django.shortcuts import render
from .exceptions import ObjectNotFoundException, InvalidDataException, ServiceException

class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        if isinstance(exception, ObjectNotFoundException):
            return render(request, 'errors/404.html', context={'error': exception.message})
        elif isinstance(exception, InvalidDataException):
            return render(request, 'errors/400.html', context={'error': exception.message})
        else:
            return render(request, 'errors/5xx.html', context={'error': exception})
