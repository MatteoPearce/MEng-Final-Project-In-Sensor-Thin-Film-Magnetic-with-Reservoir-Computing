
"""
Creates a sourcefield.txt file in specified path containing field components generated with uniform distribution
-1 < x < 1 of size row x col.
"""


import os
import warnings
from tqdm import tqdm
import random

def filemaker(output_path: str, rows: int, columns: int, field_threshold: float) -> None:

# ------------------------------------------------------------------ check inputs

    if columns is None or rows is None:
        raise ValueError('columns or rows cannot be None')

    if output_path is not None and os.path.exists(output_path):
        path_var = output_path + "/sourcefield.txt"
    else:
        path_var = "sourcefield.txt"
        warnings.warn("File path not specified/valid, output file will be created in current directory")

# ------------------------------------------------------------------ create 2D data array
    cell_num = int(columns**0.5)

    header1 = str()
    header2 = str()
    for i in range(1,cell_num+1):
        header1 = header1 + f"{i} "
        for j in range(1,cell_num+1):
            header2 = header2 + f"{i} "

    dummy = header1
    for i in range(cell_num-1):
        header1 = header1 + dummy

    header1 = header1 + "-2\n"
    header2 = header2 + "-1\n"

    data = str()
    column = str()

    for row in tqdm(range(rows)):
        for col in range(columns):

            val = round(random.uniform(-field_threshold, field_threshold), 4)

            if col == 0:
                column = column + str(val)
            else:
                column = column + " " + str(val)

        if row == 0:
            data = column +  " "  + str(row)
        else:
            data = data + "\n"  + column + " " + str(row)

        column = str()

    print(header1)
    print(header2)
    print(data)

# ------------------------------------------------------------------ write to file

    with open(path_var, "w") as file:
        file.writelines(header1)
        file.writelines(header2)
        file.writelines(str(data))

    print("\n#---------------------------------#")
    print("| SUCCESSFULLY WROTE SOURCE FILE  |")
    print("#---------------------------------#\n")



filemaker("/home/matteo/Desktop/VAMPIRE_WORKDIR", 1000,100,1)
