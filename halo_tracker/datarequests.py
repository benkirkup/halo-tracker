import httplib, urllib
import json
import settings

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'f4c6e681a0da4be094de6e222d0a58ba',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('www.haloapi.com')
    conn.request("GET", "/metadata/h5/metadata/game-base-variants?%s" % params, "{body}", headers)
    response = conn.getresponse()
    print(response)
    data = response.read()
    json_data = json.loads(data)
    print(json_data)
    # print(data)
    conn.close()

    with open(settings.BASE_DIR + '/halo_tracker/json/basevariants.json', 'w') as outfile:
        json.dump(json_data, outfile)

except Exception as e:
    print e
