FILE_PATH = '/Users/onemac/Pyhton_basics/20250721JPMC-PM/DATA/mary.txt'

with open(FILE_PATH) as mary_in:
    contents = mary_in.read()  # read entire file into one string
    print("NORMAL:")
    print(contents)
    print("=" * 20)
    print("RAW:")
    print(repr(contents))  # print string in "raw" mode
