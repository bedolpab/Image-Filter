# Import Module termcolor to change color text
from termcolor import colored

github = (colored('github.com/PabloCompSci/', 'blue'))
def info():
  error = (colored('Entering an incorrect character may result in a program malfunction', 'blue'))
  print("Welcome to Image Filter. This program allows you to apply some of our custom filters to your images.")
  print(f'When selecting a filter, please enter as proposed. {error}')
  print(f"Source code can be found on github: {github} if you would like to fork it or use it yourself")
  print(("\n") * 2) # Two new lines
  
