
# working with path --------------------------------

from pathlib import Path            # path 에 관한 library

my_path = Path("modules2/sub/__init__.py")   # creat an object about the __init__ file
# some methods from Path library
print(my_path.exists())
print(my_path.is_file())
print(my_path.is_dir())
print(my_path.name)
print(my_path.stem)
print(my_path.suffix)
print(my_path.parent)
print(my_path.with_name("new_file.py"))  # creat a new file name with the same path
print(my_path.absolute())                # absolute value of the path



# working with directory --------------------------------

# some methods I need to aware of
path = Path("sub/__init__.py")
path.exists()
path.mkdir()    # make directory
path.rmdir()    # remove directory
path.rename()   # rename
path.iterdir()  # get the list of directory and files

