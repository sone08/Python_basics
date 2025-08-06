FILE_PATH = '/Users/onemac/Pyhton_basics/20250721JPMC-PM/DATA/mary.txt'

with open(FILE_PATH) as mary_in:
    lines_without_nl = mary_in.read().splitlines()  # splitlines() splits string on '\n' into lines
    print(lines_without_nl)
