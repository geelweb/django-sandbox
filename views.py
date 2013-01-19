from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *

def home(request):
    return render_to_response(
            'home.html',
            {},
            context_instance=RequestContext(request))

def quickpoll(request):
    return render_to_response(
            'quickpoll.html',
            {},
            context_instance=RequestContext(request))

def twitter_bootstrap_form(request):
    return render_to_response(
            'twitter_bootstrap_form.html', {
                'default_form': DefaultForm(),
                'search_form': SearchForm(),
                'inline_form': LoginForm(prefix="inline"),
                'horizontal_form': LoginForm(prefix="horizontal"),
            }, context_instance=RequestContext(request))

