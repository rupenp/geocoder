Twitter Location Profile Geocoder
======================
Geoconding Twitter users' location profiles into coordinates.

"stateName,cityName" or "stateAbbreviation,cityName"

Usage
------
    yuto@tuna:~/geocoder$ python
    Python 2.7.2+ (default, Jul 20 2012, 22:15:08)
    [GCC 4.6.1] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from geocoder import Geocoder
    >>> state_abbr_filepath = 'data/state_abbr_file'
    >>> city_filepath = 'data/city_file'
    >>> gc = Geocoder(state_abbr_filepath, city_filepath)
    >>> gc.geocode('Houston, TX')
    ['29.762895', '-95.383173']
    >>> gc.geocode('Houston, Texas')
    ['29.762895', '-95.383173']
    >>> gc.geocode('Houston, MA')
    >>> gc.geocode('Boston, MA')
    ['42.321597', '-71.089115']
    >>> gc.geocode('In your heart')
    >>>

Data
------
### ``data/state_abbr_file`` ###


### ``data/city_file`` ###
 

REFERENCES
----------
[1] Z. Cheng, J. Caverlee, and K. Lee. "You are where you tweet: a content-based approach to geo-locating twitter users", In CIKM, pages 759-768, 2010.  
[2] R. Li, S. Wang, H. Deng, R. Wang, and K. C.-C. Chang. "Towards social user profiling: unified and discriminative in uence model for inferring home locations", In KDD, pages 1023-1031, 2012.

LICENSE
-------
Distributed under the [MIT License][mit].
 
[MIT]: http://www.opensource.org/licenses/mit-license.php
