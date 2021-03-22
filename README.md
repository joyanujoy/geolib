[![Build Status](https://travis-ci.org/joyanujoy/geolib.svg?branch=master)](https://travis-ci.org/joyanujoy/geolib) [![Documentation](https://readthedocs.org/projects/zodb/badge/?version=latest)](https://geolib.readthedocs.io/en/latest/) ![python 2.7|3.4|3.5|3.6|3.7](https://img.shields.io/badge/python-2.7||3.6|3.7|3.8|3.9-blue.svg) [![Downloads](https://pepy.tech/badge/geolib)](https://pepy.tech/project/geolib)

# Geolib
A python library for geohash encoding, decoding and finding neighbour cells. This is a python port of [Chris Veness' javascript implementation](https://www.movable-type.co.uk/scripts/geohash.html).

[Wikipedia reference](http://en.wikipedia.org/wiki/Geohash)
## Installation
```pipenv install geolib```
or
```pip install geolib```
## Usage

```python
from geolib import geohash
```

### Encode a latitude, longtiude to geohash

```python
>>> # geohash.encode(latitude, longitude, precision)
>>> geohash.encode('70.2995', '-27.9993', 7)
'gkkpfve'
```

### Decode a geohash to latitude, longitude

```python
>>> # geohash.decode(geohash), returns latitude, longitude as tuple of decimals
>>> geohash.decode('gkkpfve')
(70.2995, -27.9993)
```

### Find neighbouring cells of a geohash

```python
>>> # geohash.neighbours(geohash)
... # returns a namedtuple (n, ne, e, se, s, sw, w, nw)
>>> neighbours = geohash.neighbours('gcpuyph')
>>> neighbours
('gcpuypk', 'gcpuypm', 'gcpuypj', 'gcpuynv', 'gcpuynu', 'gcpuyng', 'gcpuyp5', 'gcpuyp7')
>>> neighbours.ne
'gcpuypm'
```

### Find adjacent cell in a given direction

```python
>>> # geohash.adjacent(geohash, direction)
>>> geohash.adjacent('gcpuyph', 'n')
'gcpuypk'
```

### Find SW/NE latitude/longitude bounds of a geohash
```python
>>> # geohash.bounds(geohash)
... # returns a namedtuple ((sw_lat, sw_lon), ((ne_lat, ne_lon))
>>> bounds = geohash.bounds('ezs42')
>>> bounds
((42.583, -5.625), (42.627, -5.58)))
>>> bounds.sw.lat
42.583
```
