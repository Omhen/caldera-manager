from django.shortcuts import render_to_response
from django.template import RequestContext


def not_found(request):
    return render_to_response(template_name="management_site/404.html",
                              dictionary={},
                              context_instance=RequestContext(request))