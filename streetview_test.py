from streetview import get_panorama, search_panoramas

import random

def generate_random_coordinates():
    # Generate random latitude between -90 and 90
    latitude = random.uniform(-90, 90)
    
    # Generate random longitude between -180 and 180
    longitude = random.uniform(-180, 180)
    
    return latitude, longitude


lat, lon = generate_random_coordinates()
panos = search_panoramas(lat=46.34369, lon=19.23348)

pano = panos[1]


image = get_panorama(pano.pano_id)

image.save("name.gif","GIF")