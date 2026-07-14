from typing import List , Tuple , Dict, Union

#List of integers
number : List[int] = [1,2,3,4,5]

#Tuple of a string and an integer
person : tuple[str, int] = ("Jojo",69)

#Dictionary with string keys and integer values
score : dict[str,int] = {"Jojo":69, "Bobo":67}

#Union type for variables that can hold multiple types
identifier : Union[str,int] = "ID67"
identifier = 12345 #also valid