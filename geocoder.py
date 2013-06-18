import re

class Geocoder:
    def __init__(self, state_abbr_filepath, city_filepath):
        self.state_abbr_filepath = state_abbr_filepath
        self.city_filepath = city_filepath
        self.location_dict = self.make_location_dict()
        self.state_abbr_dict = self.make_state_abbr_dict()

    def make_location_dict(self):
        location_dict = {}
        for line in open(self.city_filepath, 'r'):
            name, point = line.rstrip().split(':')
            city, state = name.lower().split('\t')
            point = point.split('\t')
            if not state in location_dict: location_dict[state] = {}
            location_dict[state][city] = point
        return location_dict

    def make_state_abbr_dict(self):
        state_abbr_dict = {}
        for line in open(self.state_abbr_filepath, 'r'):
            full, abbr = line.rstrip().lower().split(',')
            state_abbr_dict[full] = abbr 
        return state_abbr_dict

    def geocode(self, location_text):
        match = re.match('\s?(\w+)\s?,\s?(\w+)\s?', location_text.lower())
        if match == None:
            return None
        else:
            state = match.group(2)
            city = match.group(1)
            if state in self.state_abbr_dict:
                """ full name -> abbr """
                state = self.state_abbr_dict[state]
            if state in self.location_dict:
                if city in self.location_dict[state]:
                    point = self.location_dict[state][city]
                    return point
            return None
