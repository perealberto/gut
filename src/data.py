import hashlib
import os

GUT_DIR = ".gut"


def init():
    os.makedirs(GUT_DIR)
    os.makedirs(f"{GUT_DIR}/objects")
    print(f"The gut repository has been initialized at {os.getcwd()}/{GUT_DIR}")


def set_HEAD(oid):
    with open(f"{GUT_DIR}/HEAD", "w") as f:
        f.write(oid)


def hash_object(data, type_="blob"):
    obj = type_.encode() + b"\x00" + data
    oid = hashlib.sha1(obj).hexdigest()
    with open(f"{GUT_DIR}/objects/{oid}", "wb") as out:
        out.write(obj)
    return oid


def get_object(oid, expected=None):
    with open(f"{GUT_DIR}/objects/{oid}", "rb") as f:
        obj = f.read()

    type_, _, content = obj.partition(b"\x00")
    type_ = type_.decode()

    if expected is not None:
        assert type_ == expected, f"Expected {expected}, got {type_}"

    return content
