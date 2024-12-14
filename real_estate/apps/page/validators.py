""" 
Validators for the pages app and models

"""

def validate_color(r,g,b):
    if r in range(255) and g in range(255) and b in range(255):
        return True
    return False