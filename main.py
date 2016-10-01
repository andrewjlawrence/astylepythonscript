import argparse

def parseArguements():
    parser = argparse.ArgumentParser(description='Astyle python script')
    parser.add_argument('--file', nargs=1, type=str,
                    help='The file to be formatted')
    parser.add_argument('--astyle', nargs=1, type=str,
                    help='The path to the astyle executable')
    args = parser.parse_args()

def main():
    parseArguements()

if __name__ == "__main__":
    main()