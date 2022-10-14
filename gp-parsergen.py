import sys
def main():
    pass
# 2 PARAMETERS: 1. GRAMMER PATH 2. 
def usage():
    print("Usage: " + sys.argv[0] + " <grammar-file>")
if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        content = f.read()
    content_splitted = content.split("\n")
    print("compiling to" + " " + content_splitted[0][1:] + " " + "grammar")
    main()