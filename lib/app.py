# GLORY BE TO GOD,
# RUNNING PYTHON CODE, 
# CREATING A PYTHON APPLICATION - PYTHON TESTING,
# RUNNING UNIT TESTS
# BY ISRAEL MAFABI EMMANUEL

from interpolate import interpolate

def greet_user():
    name:str = input(" - What's your name? ")
    greet_text:str = "Hello,"
    print(interpolate(greet_text, name))

greet_user()