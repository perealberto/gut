import argparse
import os
from . import data


def main():
    try:
        args = parse_arguments()
        args.func(args)
    except Exception as e:
        raise e
    except KeyboardInterrupt:
        print("Exiting gut! >:(")


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="gut",
        description="(G)it (U)nique implemen(T)ation is a simple implementation of the famous version control system Git!",
        add_help=True,
    )

    commands = parser.add_subparsers(title="command")
    commands.required = True

    init_parser = commands.add_parser("init")
    init_parser.set_defaults(func=init)

    hash_object_parser = commands.add_parser("hash-object")
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument("file")

    return parser.parse_args()


def init(args):
    data.init()
    print(f"The gut repository has been initialized at {os.getcwd()}/{data.GUT_DIR}")


def hash_object(args):
    with open(args.file, "rb") as f:
        print(data.hash_object(f.read()))
