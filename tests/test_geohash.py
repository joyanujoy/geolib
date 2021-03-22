import pytest
import decimal
from geolib import geohash


def test_bounds():
    bounds = geohash.bounds("ezs42")
    assert (bounds.sw.lat, bounds.sw.lon) == pytest.approx((42.583, -5.625), rel=1e-3)
    assert (bounds.ne.lat, bounds.ne.lon) == pytest.approx((42.627, -5.58), rel=1e-3)


def test_decode():
    decimal.getcontext().prec = 7
    expected = (decimal.Decimal("42.60498046875"), decimal.Decimal("-5.60302734375"))
    rel = decimal.Decimal("1e-3")
    assert geohash.decode("ezs42") == pytest.approx(expected, rel=rel)


def test_encode():
    assert geohash.encode("68", "-23", 1) == "g"
    assert geohash.encode("70.3", "-28", 2) == "gk"
    assert geohash.encode("70.2995", "-27.9993", 7) == "gkkpfve"


def test_neighbours():
    neighbours = geohash.neighbours("gcpuyph")
    neighbours.n == "gcpuypk"
    neighbours.s == "gcpuynu"
    neighbours.e == "gcpuyp5"
    neighbours.w == "gcpuypj"
    neighbours.nw == "gcpuyp7"
    neighbours.ne == "gcpuypm"
    neighbours.se == "gcpuynv"
    neighbours.sw == "gcpuyng"


def test_neighbours_london():
    neighbours = geohash.neighbours("gcpvn0c")
    neighbours.n == "gcpvn11"
    neighbours.s == "gcpvn09"
    neighbours.e == "gcpvn0f"
    neighbours.w == "gcpvn0b"
    neighbours.nw == "gcpvn10"
    neighbours.ne == "gcpvn14"
    neighbours.se == "gcpvn08"
    neighbours.sw == "gcpvn0d"
