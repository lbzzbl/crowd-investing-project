from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.models import User, RegistrationForm

def index(request):
    template = 'index.html'
    registration = RegistrationForm()

    return render_to_response('index.html', {'registration': registration},
        context_instance=RequestContext(request))

def register(request):
	  