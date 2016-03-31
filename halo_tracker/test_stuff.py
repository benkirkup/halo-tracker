import json
import django
from halo_project import settings
import os

def parse_json_file():

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "halo_project.settings")
    django.setup()

    variant_list = []

    json_file = open(settings.BASE_DIR + '/halo_tracker/json/basevariants.json', 'r')
    json_data = json.load(json_file)

    for jsonData in json_data[0:13]:
        if not jsonData['name']:
            jsonData['name'] = 'Forge'

        print jsonData['name']
        variant_list.append({jsonData['name']: jsonData['contentId']})

    print variant_list

    for item in variant_list:
        models.gameVariants.objects.create(name=item['name'], contentId=item['contentId'])


if __name__ == '__main__':
    parse_json_file()