n : int = 5             # varibale marked as int => when we type n. we will be suggested with all the integers methods out there

name : str = "Miyoko"   # varibale marked as string


# in fns :

def sum(a:int , b:int) -> int:          # -> means the fn will return integer value 
    return a+b

sum(3,8)


# Advaced type


from typing import List, Tuple, Dict, Union 

# List of integers 
numbers: List[int] = [1, 2, 3, 4, 5] 

# Tuple of a string and an integer 
person: Tuple[str, int] = ("Alice", 30) 

#  Dictionary with string keys and integer values 
scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 

# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123"
identifier = 12345  # Also valid 