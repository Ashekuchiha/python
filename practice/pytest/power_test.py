from power import poww

def pos () :
    assert poww(2) == 4
    assert poww(3) == 9
def neg () :
    assert poww(-2) == 4
    assert poww(-3) == 9
def zero () :
    assert poww(0) == 0

pos()
neg()
print("ji")
zero()