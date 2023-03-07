import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', action='store')
    args = parser.parse_args()
    with open(args.file, "r") as f:
        content = f.read()
    content_splitted = content.split("\n")
    if content_splitted[0][0] != '!':
        raise ValueError('No language specified')
    language = content_splitted[0][1:]
    print("compiling to" + " " + language + " " + "grammar")


if __name__ == '__main__':
    main()
