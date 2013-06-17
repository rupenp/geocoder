import sys
from geocoder import Geocoder

if len(sys.argv) < 4:
    print "[USAGE]: python %s [state abbr filepath] [city filepath] [location text filepath]" % sys.argv[0]
    exit()

state_abbr_filepath = sys.argv[1]
city_filepath = sys.argv[2]
location_text_filepath = sys.argv[3]

gc = Geocoder(state_abbr_filepath, city_filepath)

for line in open(location_text_filepath, 'r'):
    location_text = line.rstrip()
    point = gc.geocode(location_text)
    if point == None:
        print None
    else:
        print point[0], point[1]
