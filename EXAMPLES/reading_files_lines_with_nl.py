FILE_PATH = '/Users/onemac/Pyhton_basics/20250721JPMC-PM/DATA/mary.txt'

with open(FILE_PATH) as mary_in:
    lines_with_nl = mary_in.readlines()  # readlines() reads all lines into an array
    print(lines_with_nl)
