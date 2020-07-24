""" kwargs (Keyword Arguments) intro"""

def func(**kwargs): # pass as a dictionary
    for k,v in kwargs.items():
        print(k,v)

dict1 = {'name' : 'nateq', 'surname' : 'siddiqui'}
func(**dict1) #kwargs unpacking

"""Sequence of arguments in functions"""

# PADK

# parameteres
# *args
# default parameters
# **kwargs