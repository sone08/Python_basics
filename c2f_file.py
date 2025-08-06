FILE_PATH = '/Users/onemac/Pyhton_basics/20250721JPMC-PM/DATA/ctemps.txt'

import os
file_name=FILE_PATH
temp_name="ftemps.txt"
# Convert Celsius to Fahrenheit and write to a new file
with open(file_name) as ctemps_in:
    with open(temp_name, 'w') as ftemps_out:
        for raw_line in ctemps_in:
            line = raw_line.rstrip()  # remove trailing whitespace
            if line:  # check if line is not empty
                celsius = float(line)  # convert string to float
                fahrenheit = (celsius * 9/5) + 32  # convert to Fahrenheit
                ftemps_out.write(f"{fahrenheit:.2f}\n")  # write to output file with two decimal places
                print(f"{celsius:.2f} C = {fahrenheit:.2f} F")  # print conversion to console