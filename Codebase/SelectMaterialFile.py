import os

"""
RECEIVES DESIRED MATERIAL FILE NAME, PARSES THE MATERIALS FOLDER IN THE WORKING DIRECTORY AND COPIES THE CORRECT FILE 
TO THE WORKING DIRECTORY AFTER HAVING REMOVED THE EXISTING MATERIAL FILE.
"""
def select_material(file_name: str = None, file_path: str = None, workdir_path: str = None) -> None:

    if file_path is not None and file_name is not None and workdir_path is not None:
        if file_path == workdir_path:
            raise Exception("file path cannot be same as workdir path")

        for file in os.listdir(workdir_path):
            filename = os.fsdecode(file)
            if filename.endswith(".mat"):
                os.remove(os.path.join(workdir_path, file))


        with open(file_path + "/" + file_name, 'r') as file:
            data = file.readlines()
            file.close()
        if data is not None:
            print("successfully grabbed material file \n")

        with open(workdir_path + "/" + file_name, 'w') as file:
            file.writelines(data)
            file.close()
            print("successfully copied material file to workdir \n")
