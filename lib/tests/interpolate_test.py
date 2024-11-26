# GLORY BE TO GOD,
# TESTING FILE
# BY ISRAEL MAFABI EMMANUEL

from interpolate import interpolate

def test_interpolation():
    assert(interpolate("Hello,", "Wendy") == "Hello, Wendy!") # test case 1
    assert(interpolate("Hello,", "Emmanuel") == "Hello, Emmanuel!") # test case 2