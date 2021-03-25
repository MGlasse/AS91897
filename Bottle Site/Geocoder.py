import sys

from pygeocoder import Geocoder
from pygeolib import GeocoderError

try:
  address = Geocoder.geocode('3 fergy cres, wattle downs, auckland, new zealand '.join(sys.argv[1:]))
except GeocoderError:
  print ("The address entered could not be geocoded")
  sys.exit()

if not address.valid_address:
  print ("The address entered is not valid, but we did get some info")

print ("address.valid_address: ", address.valid_address)
