Twitter Location Profile Geocoder
======================
Geoconding Twitter users' location profiles into coordinates.

"stateName,cityName" or "stateAbbreviation,cityName"

Usage
------
### Make input data ###
    $ cat data/test_data
    Houston, Texas
    Houston, TX
    Boston, MA
    Boston ,MA
    Boston , MA
    Houston, MA
    In your heart

### Geocode prepared input data ###
    $ python main.py data/state_abbr_file data/city_file data/test_data
    29.762895 -95.383173
    29.762895 -95.383173
    42.321597 -71.089115
    42.321597 -71.089115
    42.321597 -71.089115
    None
    None

Data
------
### data/state_abbr_file ###
``[Full state name],[state abbreviation]`` for each line.

    $ head -5 data/state_abbr_file
    Alabama,AL
    Alaska,AK
    Arizona,AZ
    Arkansas,AR
    California,CA

### data/city_file ###
``[city name]\t[state abbreviation]:[latitude]\t[longitude]`` for each line.

    $ head -5 data/city_file
    Abbeville       AL:31.566367    -85.251300
    Abbeville city  AL:31.566367    -85.251300
    Adamsville      AL:33.590411    -86.949166
    Adamsville city AL:33.590411    -86.949166
    Addison AL:34.200042    -87.177851

REFERENCES
----------
[1] Z. Cheng, J. Caverlee, and K. Lee. "You are where you tweet: a content-based approach to geo-locating twitter users", In CIKM, pages 759-768, 2010.  
[2] R. Li, S. Wang, H. Deng, R. Wang, and K. C.-C. Chang. "Towards social user profiling: unified and discriminative in uence model for inferring home locations", In KDD, pages 1023-1031, 2012.

LICENSE
-------
Distributed under the [MIT License][mit].
 
[MIT]: http://www.opensource.org/licenses/mit-license.php
