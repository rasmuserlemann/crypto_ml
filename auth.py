import os
__location__ = os.path.realpath(
os.path.join(os.getcwd(), os.path.dirname(__file__)))
def check(code):
    f = open(os.path.join(__location__, 'codes.txt'),  "r")
    if str(code) in f.read():
        return(True)
    else:
        return(False)
