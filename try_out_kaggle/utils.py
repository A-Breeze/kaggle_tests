""""Useful functions to use in the notebook 'Try_out_Kaggle'"""

#########
# Setup #
#########
# Module variables
__version__ = '0.1.0'  # Useful for checks when running the notebook

# Import built-in modules
from pathlib import Path

# Import external modules
# [None yet]

#################################
# Visualise directory structure #
#################################
def tree(dir_path: Path, prefix: str=''):
    """
    A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    
    Adapted from here: <https://stackoverflow.com/a/59109706>
    
    Examples:
        >>> for line in tree(Path.home()):
        >>>      print(line)
    """
    # prefix components:
    space =  '    '
    branch = '│   '
    # pointers:
    tee =    '├── '
    last =   '└── '
    
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space 
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)
