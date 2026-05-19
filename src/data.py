import hashlib
import os

GUT_DIR = ".gut"


def init():
    os.mkdir(GUT_DIR)
    os.makedirs(f"{GUT_DIR}/objects")


def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(f"{GUT_DIR}/objects/{oid}", "wb") as f:
        f.write(data)
    return oid


def get_object(oid):
    with open(f"{GUT_DIR}/objects/{oid}", "rb") as f:
        return f.read()
