"""This module provides the views for the explorer interface."""

import json
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
import nbformat
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup
from mpcontribs.client import load_client

def index(request):
    ctx = RequestContext(request)
    try:
        client = load_client()
        resp = client.projects.get_entries(mask=['project']).response()
        ctx['projects'] = [r['project'] for r in resp.result]
    except Exception as ex:
        ctx['alert'] = f'{ex}'
    return render(request, "mpcontribs_explorer_index.html", ctx.flatten())

def export_notebook(nb, cid):
    nb = nbformat.from_dict(nb)
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
    body = html_exporter.from_notebook_node(nb)[0]
    soup = BeautifulSoup(body, 'html.parser')
    # mark cells with special name for toggling, and
    # TODO make element id's unique by appending cid (for ingester)
    for div in soup.find_all('div', 'output_wrapper'):
        script = div.find('script')
        if script:
            script = script.contents[0]
            if script.startswith('render_json'):
                div['name'] = 'HData'
            elif script.startswith('render_table'):
                div['name'] = 'Table'
            elif script.startswith('render_plot'):
                div['name'] = 'Graph'
        else:
            pre = div.find('pre')
            if pre and pre.contents[0].startswith('Structure'):
                div['name'] = 'Structure'
    # name divs for toggling code_cells
    for div in soup.find_all('div', 'input'):
        div['name'] = 'Code'
    # separate script
    script = []
    for s in soup.find_all('script'):
        script.append(s.text)
        s.extract() # remove javascript
    return soup.prettify(), '\n'.join(script)

def contribution(request, cid):
    ctx = RequestContext(request)
    client = load_client()
    nb = client.notebooks.get_entry(cid=cid).response().result
    ctx['nb'], ctx['js'] = export_notebook(nb, cid)
    return render(request, "mpcontribs_explorer_contribution.html", ctx.flatten())

def cif(request, sid):
    client = load_client()
    cif = client.structures.get_cif(sid=sid).response().result
    if cif:
        return HttpResponse(cif, content_type='text/plain')
    return HttpResponse(status=404)

def download_json(request, cid):
    client = load_client()
    contrib = client.contributions.get_entry(cid=cid).response().result
    if contrib:
        jcontrib = json.dumps(contrib)
        response = HttpResponse(jcontrib, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename={}.json'.format(cid)
        return response
    return HttpResponse(status=404)
