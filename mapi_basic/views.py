import json
from urllib import unquote
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseServerError
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'POST':
        api_key = request.POST.get('apikey')
        if api_key == 'None': api_key = None
        try:
            from .models import RegisteredUser
            u = RegisteredUser.objects.get(username=request.user.username)
            if api_key: u.api_key = api_key
            u.save()
        except Exception, e:
            return HttpResponseServerError(str(e))
    from test_site.settings import INSTALLED_APPS
    apps = [
        app.replace('.', '/') for app in INSTALLED_APPS
        if 'django' not in app and 'mapi_basic' not in app
    ]
    ctx = RequestContext(request)
    return render_to_response("index.html", locals(), ctx)

@login_required
def register(request):
    """Register the user."""
    from .models import RegisteredUser, RegisteredUserForm
    email = request.user.email
    username = request.user.username
    u = RegisteredUser.objects.get(username=username)
    name = "%s %s" % (request.user.first_name, request.user.last_name)
    next = unquote(request.GET.get('next', '/'))
    if next == '/register':
        next = '/'
    if request.method == "GET":
        if u.is_registered:
            return redirect(next)
        form = RegisteredUserForm()
    else:
        form = RegisteredUserForm(request.POST, instance=u)
        if form.is_valid():
            u.is_registered = True
            u.institution = form.cleaned_data['institution']
            u.save()
            return redirect(next)
    return render_to_response('register.html', locals(),
                              RequestContext(request))
