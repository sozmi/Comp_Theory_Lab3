import pytest
from res.player_base import Base
from res.unit_enum_factory import Units

#найм юнитов
def test_unit_recruitment():
    b = Base()
    for i in range(b.max_unit_amount + 3):
        b.recruit_unit(Units(1))
    assert b.unit_amount <= b.max_unit_amount
#найм юнитов неверный ввод
def test_unit_rectuitment_wrong_input():
    b = Base()
    with pytest.raises(ValueError): 
        b.recruit_unit('a')
#найм юнитов неверный ввод 2
def test_unit_rectuitment_wrong_input2():
    b = Base()
    with pytest.raises(ValueError): 
        b.recruit_unit(Units(-999))
#удаление юнитов
def test_remove_unit():
    b = Base()
    for i in range(b.max_unit_amount + 1):
        b.recruit_unit(Units(1))
    b.remove_unit()
    assert b.unit_amount == b.max_unit_amount - 1
#удаление юнитов неверный ввод
def test_remove_unit2():
    b = Base()
    for i in range(b.max_unit_amount + 1):
        b.recruit_unit(Units(1))
    for i in range(b.max_unit_amount + 1):
        b.remove_unit()
    assert b.unit_amount == 0
