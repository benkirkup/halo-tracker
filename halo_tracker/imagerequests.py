import httplib, urllib, base64

def save_spartan_image(player_names):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'f4c6e681a0da4be094de6e222d0a58ba',
    }

    try:
        for player_name in player_names:
            conn = httplib.HTTPSConnection('www.haloapi.com')
            player_name_url = player_name.replace(' ', '%20')
            conn.request("GET", "/profile/h5/profiles/%s/spartan" % player_name_url, "{body}", headers)
            response = conn.getresponse()
            spartan_url = response.msg['Location']
            print(player_name + " spartan image get successful")
            conn.close()
            player_name_file = player_name.replace(' ', '_')
            urllib.urlretrieve(spartan_url, 'C:\VMShared\halo_project\static\img\%s.png' % player_name_file)
        print("All spartan images successfully retrieved")
    except Exception as error:
        print(error)

def save_emblem(player_names):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'f4c6e681a0da4be094de6e222d0a58ba',
    }

    try:
        for player_name in player_names:
            conn = httplib.HTTPSConnection('www.haloapi.com')
            player_name_url = player_name.replace(' ', '%20')
            conn.request("GET", "/profile/h5/profiles/%s/emblem" % player_name_url, "{body}", headers)
            response = conn.getresponse()
            spartan_url = response.msg['Location']
            print(player_name + " emblem image get successful")
            conn.close()
            player_name_file = player_name.replace(' ', '_')
            urllib.urlretrieve(spartan_url, 'C:\VMShared\halo_project\static\img\%s_emblem.png' % player_name_file)
        print("All emblems successfully retrieved")

    except Exception as error:
        print(error)


if __name__ == '__main__':
    player_list = ['cptsponge ii', 'syphen d664', 'mrsnesbitt90']
    save_spartan_image(player_list)
    save_emblem(player_list)