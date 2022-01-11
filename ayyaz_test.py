from Point import Point
import pytest

def test():
   p = Point("RWP",10,20)
   assert p.get_lan_long() == (10,20)

def test_2():

    with pytest.raises(Exception) as ex:
       p = Point("RWP",-1 , 20)
    assert ex.type == ValueError

def test_3():

    with pytest.raises(Exception) as ex:
       p = Point("RWP",-1 , 20)
    assert ex.type == ValueError

    with pytest.raises(Exception) as ex:
       p = Point(5,-1 , 20)
    assert str(ex.value) == "City name should be String"