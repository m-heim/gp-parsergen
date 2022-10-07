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
    main()