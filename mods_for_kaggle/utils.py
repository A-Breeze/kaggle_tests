"""Useful functions to use in the notebook 'Try_out_Kaggle'"""

#########
# Setup #
#########
# Module variables
__version__ = '0.2.0'  # Useful for checks when running the notebook

# Import built-in modules
from urllib.request import urlopen

# Import external modules
# [None yet]

##############################
# Interact with the internet #
##############################
def is_internet_accessible(test_address='https://www.google.com/'):
    """Quick test to see whether we can access the internet"""
    try:
        response = urlopen(test_address, timeout=10)
        return True
    except: 
        return False

