from pyramid.renderers import get_renderer
from pyramid.view import view_config

def site_layout():
    renderer = get_renderer("templates/layout.pt")
    layout = renderer.implementation().macros['layout']
    return layout

@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    return {  'layout' : site_layout(),
                    'project':'TapMap'}

@view_config(route_name='logon', renderer='templates/logon.pt')
def logon(request):
    return {  'layout' : site_layout(),
                    'project':'TapMap'}