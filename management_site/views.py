from django.shortcuts import render_to_response
from django.template import RequestContext
from config import settings
from helpers.config_manager import ConfigManager
from management_site import validator
from management_site.error_views import not_found


CALDERA_CONFIG_FILE = getattr(settings, 'CALDERA_CONFIG_FILE')
CONF_SECTION = 'Times'

def index(request):
    context = {}
    config_manager = ConfigManager(CALDERA_CONFIG_FILE)
    context['variables'] = config_manager.get_all(CONF_SECTION)
    return render_to_response(template_name='management_site/index.html',
                              dictionary=context,
                              context_instance=RequestContext(request))


def change_variables(request):
    config_manager = ConfigManager(CALDERA_CONFIG_FILE)
    for key, value in request.POST.iteritems():
        if validator.is_empty(value):
            continue
        validator.is_int(key, value)
        config_manager.put(CONF_SECTION, key, value)
    config_manager.flush()
    context = {
        'variables': config_manager.get_all(CONF_SECTION)
    }
    return render_to_response(template_name='management_site/index.html',
                              dictionary=context,
                              context_instance=RequestContext(request))


def http404(request):
    return not_found(request)