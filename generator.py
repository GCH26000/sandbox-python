from sre_parse import SPECIAL_CHARS
import string
import random

def hello_world():
    return "Hello world !"


def generatePassword(length):
    l = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(SPECIAL_CHARS)
    password = "".join(random.choices(l, k=length))
    return password