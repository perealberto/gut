import hashlib
import os

GUT_DIR = ".gut"


def init():
    os.mkdir(GUT_DIR)
    os.makedirs(f"{GUT_DIR}/objects")
    print(f"The gut repository has been initialized at {os.getcwd()}/{GUT_DIR}")


def hash_object(data, _type="blob"):
    obj = _type.encode() + b"\x00" + data
    oid = hashlib.sha1(obj).hexdigest()
    with open(f"{GUT_DIR}/objects/{oid}", "wb") as f:
        f.write(obj)
    return oid


def get_object(oid, expected=None):
    with open(f"{GUT_DIR}/objects/{oid}", "rb") as f:
        obj = f.read()

    _type, _, content = obj.partition(b"\x00")
    _type = _type.decode()

    if expected is not None:
        assert _type == expected, f"Expected {expected}, got {_type}"

    return content
