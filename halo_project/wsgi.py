"""
WSGI config for halo_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import json
import settings
from halo_tracker import models

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "halo_project.settings")

application = get_wsgi_application()

# Update game variants
variant_list = []

json_file = open(settings.BASE_DIR + '/halo_tracker/json/basevariants.json', 'r')
json_data = json.load(json_file)

for jsonData in json_data[0:13]:
    if not jsonData['name']:
        jsonData['name'] = 'Forge'

    variant_list.append({'name': jsonData['name'], 'id': jsonData['contentId']})


for item in variant_list:
    models.gameVariants.objects.update_or_create(name=item['name'], contentId=item['id'])