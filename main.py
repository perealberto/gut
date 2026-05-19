import argparse
from src import gutlib as gl


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="gut",
        description="(G)it (U)nique implemen(T)ation is a simple implementation of the famous version control system Git!",
        add_help=True,
    )

    commands = parser.add_subparsers(
        title="command",
        description="Action commands",
    )
    commands.required = True

    init_parser = commands.add_parser("init", help="Initialize repository")
    init_parser.set_defaults(func=gl.init)

    commands.add_parser("status", help="Prints the current status of the repository")

    return parser.parse_args()


def main():
    args = parse_arguments()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise e
    except KeyboardInterrupt:
        print("Exiting program!")
