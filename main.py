""" Import's
| 'PIL' Pillow module for images
| 'datetime' module for counter
| 'termcolor' module for string color
| code files 'info_start' and 'ascii'
| 'os' module for checking existing images
"""

from PIL import Image, ImageFilter, ImageEnhance
from termcolor import colored
from info_start import info
from ascii import ascii_display
import time
import os


###                  ###
##  Filter Functions  ##
###                  ### 

""" Invert Function
| Function: invert_distort()
| Parameters: display_algorithm, image_filter_inverted
| ------
| Filter one:
| In this filter, the colors of the image are inverted,
| that being either into negative or monochrome colors.
| For this filter to be applied, user must choose
| 'Inverted' and then either 'negative' or 'monochrome'.
| ------
| 1.) Pixels from the original image are recieved, using 
|     .getdata() method, then stored in pixel_list[]
| 2.) Every pixel is then modified based off users
|     selection of filter.
| 2.a) Before color modification, user is allowed 
|      to choose if they want to see the algorithm
|      do its job (back-end).
| 3.) Colors are assigned, stored into final_mage, applied
|     an extra sharpen filtered, then the image gets stored
|     into filter_applied. The final Image is then returned.
| More info can be found in comments below
"""
# Filter One
def invert_distort(display_algorithm, image_filter_inverted):
  # Get pixel data (every pixel) and make new list
  pixels_get = img.getdata() 
  pixel_list = [] 

  # Go through every pixel in image and append every pixel to list
  for p in pixels_get: 
    pixel_list.append(p) 

  # Pixel location and row 
  pixel_location = 0
  pixel_row = 0

  # Begin while loop at index 0 in order to loop through every pixel
  while pixel_location < len(pixel_list): 
    p = pixel_list[pixel_location] 

    # Prints current row and pixel color values
    if display_algorithm == 'y':
      print(f'Current row: {pixel_row}: {p}')
      pixel_row += 1

    if display_algorithm == 'n': 
      pass

    # Pixel Manipulation
    # If user enters accordingly, Colors Red, Green, Blue set into variables
    xr, xg, xb = 0, 0, 0

    if image_filter_inverted in image_filter_inverted_choices[0]:
      xr, xg, xb = 0, 1, 2

    elif image_filter_inverted in image_filter_inverted_choices[1]:
      xr, xg, xb = 2, 2, 2
   
    # Red, Green, Blue sorted into pixel list
    r, g, b = p[xr], p[xg], p[xb]

    # RGB values assigned to r, g, b
    absr, absg, absb = 255, 255, 255

    # Absolute value of pixels from red, green blue taken.
    # RBG values assigned, stored into variables below.
    update_r, update_g, update_b = abs(r-absr), abs(g-absg), abs(b-absb)

    # New values assigned at specific pixel location
    pixel_list[pixel_location] = (update_r, update_g, update_b)
    pixel_location = pixel_location + 1
    
  # New image created using same size and RGB format
  final_image = Image.new("RGB", img.size)
  final_image.putdata(pixel_list)
  
  # Filter from PIL applied to new image
  filter_applied = final_image.filter(ImageFilter.SHARPEN)
  return filter_applied


""" Drawing Function
| Function: drawing_filter()
| Parameters: display_algorithm, image_filter_drawing
| ------
| Filter two:
| In this filter, the colors of the image are adjusted
| to black and white, or white and black, which will
| then be adjusted to a specific drawing style based
| off the users choice. For this filter to be applied,
| the user must choose 'Drawing', and then either
| 'sketch' or 'engraving'.
| ------
| 1.) Pixels from the original image are recieved, using
|     .get() method, then stored in pixe_list[].
| 2.) Every pixel is then modified based off users
|     selection of filter.
| 2.a) Before color modification, user is allowed to
|      choose if they want to see the algorithm do
|      its job (back-end).
| 3.) Colors are assigned, stored into final_mage, applied
|     an extra contour or emobss filter to create the drawing
|     style. Then, the image gets stored into filter_applied. 
|     The final Image is then returned.
| More info can be found in comments below
"""
# Filter Two
def drawing_filter(display_algorithm, image_filter_drawing):

  # Get pixel data (every pixel) and make new list
  pixels_get = img.getdata() 
  pixel_list = [] 

  # Go through every pixel in image and append every pixel to list
  for p in pixels_get: 
    pixel_list.append(p) 

  # Pixel location and row 
  pixel_location = 0
  pixel_row = 0

  # Begin while loop at index 0 in order to loop through every pixel
  while pixel_location < len(pixel_list): 
    p = pixel_list[pixel_location] 

    # Prints current row and pixel color values
    if display_algorithm == 'y':
      print(f'Current row: {pixel_row}: {p}')
      pixel_row += 1

    if display_algorithm == 'n': 
      pass

    # Pixel Manipulation
    # Colors Red, Green, Blue set into variables
    xr, xg, xb = 2, 2, 2

    # Red, Green, Blue sorted into pixel list
    r, g, b = p[xr], p[xg], p[xb]

    # RGB values assigned to r, g, b
    absr, absg, absb = 255, 255, 255

    # Absolute value of pixels from red, green blue taken.
    # RBG values assigned, stored into variables below.
    update_r, update_g, update_b = abs(r-absr), abs(g-absg), abs(b-absb)

    # New values assigned at specific pixel location
    pixel_list[pixel_location] = (update_r, update_g, update_b)
    pixel_location = pixel_location + 1

  # New image created using same size and RGB format
  final_image = Image.new("RGB", img.size)
  final_image.putdata(pixel_list)

  # If statement applies, filter added to new image
  # Filter from PIL applied to new image
  if image_filter_drawing in image_filter_drawing_choices[0]:
    filter_applied = final_image.filter(ImageFilter.CONTOUR)
    return filter_applied

  elif image_filter_drawing in image_filter_drawing_choices[1]:
    filter_applied = final_image.filter(ImageFilter.EMBOSS)
    return filter_applied


""" Contrast Function
| Function: contrast_filter()
| Parameters: display_algorithm
| ------
| Filter three:
| In this filter, the colors of the image are not changed, but
| each pixel is still stored if desired to change in the future.
| all that is applied is a contrast filter. For this filter to be
| applied, the user must choose 'Contrast'. 
| ------
| 1.) Pixels from the original image are recieved, using
|     .get() method, then stored in pixe_list[].
| 2.) Every pixel is stored, but not modified.
| 2.a) Before color modification, user is allowed to
|      choose if they want to see the algorithm do
|      its job (back-end).
| 3.) Original colors are stored into final_image, and then the
|     contrast filter is applied. The final Image is then returned.
| More info can be found in comments below
"""
# Filter Three
def contrast_filter(display_algorithm): 

  # Get pixel data (every pixel) and make new list
  pixels_get = img.getdata() 
  pixel_list = [] 

  # Go through every pixel in image and append every pixel to list
  for p in pixels_get: 
    pixel_list.append(p) 

  # Pixel location and row 
  pixel_location = 0 
  pixel_row = 0 

  # Begin while loop at index 0 in order to loop through every pixel
  while pixel_location < len(pixel_list): 
    p = pixel_list[pixel_location] 

    # Prints current row and pixel color values
    if display_algorithm == 'y':
      print(f'Current row: {pixel_row}: {p}')
      pixel_row += 1
      
    if display_algorithm == 'n': 
      pass

    # Pixel Manipulation
    # Colors Red, Green, Blue set into variables
    xr, xg, xb = 0, 1, 2

    # Red, Green, Blue sorted into pixel list
    r, g, b = p[xr], p[xg], p[xb]

    # RBG values assigned, stored into variables below.
    update_r, update_g, update_b = r, g, b

    # New values assigned at specific pixel location
    pixel_list[pixel_location] = (update_r, update_g, update_b)
    pixel_location = pixel_location + 1

  # New image created using same size and RGB format
  final_image = Image.new("RGB", img.size)
  final_image.putdata(pixel_list)  

  # First Enhance Applied
  applyOne = ImageEnhance.Contrast(final_image)
  # Second Enhance Applied
  applyTwo = applyOne.enhance(0.5)
  # Final form stored into new variable
  filter_applied = applyTwo
  return filter_applied
  

###                   ###
##    ASCII, Info,     ##
##  & Image Selection  ##
###                   ### 

# Function ASCII made in ascii.py
ascii_display()

# Function info() made in info_start.py
info()


""" Appearance Countdown
| Timer to give user time
| to read information and
| what the program does 
"""
for i in range(5, 0, -1): # count down from 5
  time.sleep(1) # delay 1 seconds
  print(f'Program initiating in {i}')
print(('\n') * 2) # Two new lines


""" Previous Image Deletion
| Deletes previous images that
| have been generated 
"""
images = ['InvertIMG.jpg', 'DrawingIMG.jpg', 'ContrastIMG.jpg']
for i in images: # per image in list
  if os.path.exists(i): # if exists
    os.remove(i) # remove if exists


""" Image Selection
| 1.) Prints image options with description
| 2.) img_choices assigns images a char
| 3.) while loop to select image based off user
|     input and its assigned char (plus error prevention)
| ------
| * Image.open will open image inside ()
"""
print("What image would you like to utilize? City Image: 'A', Dog Image: 'B', or Statue of Liberty: 'C'")

# Assign image choice char
img_choices = ['a', 'b', 'c']

# while loop for image choice
while True:
  # Image selection input
  img_input = input('Choose Image: ').casefold()
  # If Statements for opening image of choice
  if img_input == img_choices[0]:
    img = Image.open('subjectIMG.jpg')
    break # exits loop
  elif img_input == img_choices[1]:
    img = Image.open('subjectIMG0.jpg')
    break # exits loop
  elif img_input == img_choices[2]:
    img = Image.open('subjectIMG2.jpg')
    break # exits loop
  elif img_input != img_choices:
    print(colored("\nError: Please enter 'A', 'B', or 'C' from the choices above\n", 'red'))
else:
  pass


""" Appearance Time Suspend
| Only for aesthetic appearance
| You can remove if you'd like
| Removing will not impact program
| ------
| * time.sleep() method suspends program for 
| the sugested time entered inside ()
| ex: current time it's suspending is 1 second
"""
# For visuals only
time.sleep(0.8), print('\nChoosing your image....\n')
time.sleep(0.8), print('Image choosen!\n'), time.sleep(0.8)


""" Image Scale
| Rescales image to appropriate or preferred size
| * Size that's preferred by programmer, not user*
| ------
| * 'img.' is the image that was choosen above
| based off current height and width, hence
|
| * .width and .height, it will scale to 
| preferred heigh in xwidth and yheight variables
"""
# Rescales image to preferred size
width, height = img.width, img.height
xwidth, yheight = width // 1000, height // 1000
if xwidth > yheight:
  scale = xwidth
else:
  scale = yheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )


###                                      ###
##   Algorithm Vizualitaion Selection,    ##
##           Filter Selection,            ##
##         & Sub-Filter Selection         ##
###                                      ### 

""" Algorithm Vizualization Choice
| User is given option to see the pixel manipulation
| and filter appliction's algorithm do its job (back-end). 
| They are given the options of Yes: 'y' or No: 'n'.
| ------
| * display_choices is list with the string inputs the user
| must enter to chose yes or no.
|
| * while loop prevents input error (user entering something
|   that they were not prompted to enter). Input must
|   match prompted choices, else error statement to re-enter
|   will be prompted (more info in comemnts below).
"""
# Display Algorithm choices
display_choices = ['y', 'n'] # display algorithm choices

# while loop to prevent display_algorithm input error
while True:
  display_algorithm = input("Would you like to see the back-end (algorithm) process? Enter 'Y' or 'N': ").casefold()
  # If input found in choice list, accept
  if display_algorithm in display_choices:
    break # exit loop

  # If input not found in choice list, reject input and try again
  elif display_algorithm != display_choices:
    print(colored("\nError: Please enter 'Y' or 'N'\n", 'red'))
    False # retry while loop


""" Filter Choice
| User is given the option to have the filter inverted, 
| drawing, or contrast be applied to their selected
| image of choice. They must select 'a', 'b', or 'c'.
| ------
| * image_filter_main_choices is list with the string inputs
|   the user must enter to choose a filter.
|
| * while loop prevents input eror (user entering something
|   that they were not prompted to enter). Input must
|   match prompted choices, else error statement to re-enter
|   will be prompted (more info in comemnts below).
"""
# Main Filter choices
image_filter_main_choices = ['a', 'b', 'c']

# while loop to prevent image_filter_main input error
while True:
  image_filter_main = input("\nChoose a filter: Inverted: 'A', Drawing: 'B', or Contrast: 'C': ").casefold()
  # If input found in choice list, accept
  if image_filter_main in image_filter_main_choices:
    break # exit loop

  # If input not found in choice list, reject input and try again
  elif image_filter_main != image_filter_main_choices:
    print(colored("\nError: Please try 'A', 'B', or 'C' from the choices above\n", 'red'))
    False


""" Time Module
| Functions are called to initiate the filter application. 
| (sub-filter choices are also prompted)
| # Functions called: invert_distort(), drawing_filter(), contrast_filter()
"""
#'time' module for counter
from datetime import datetime


###                    ###
##  Filter Application  ##
###                    ### 

""" Inverted Filter
| If statement for inverted filter:
| Based off input choice (also with sub-filter)
| choice, function invert_distort() is called to apply
| appropriate filter. Input prevention error while
| loop is also included in inverted filter if statement.
| Once filter applied, final image is stored in imageInvert
| variable and saved as 'InvertIMG.jpg'.
| ------
| module 'datetime' is used below to track total time
| taken to execute filter application. Total time
| take is printed for user to see.


"""
# Function invert_distort() if statment
if image_filter_main in image_filter_main_choices[0]:

  # Image Filter Inverted choices
  image_filter_inverted_choices = ['a', 'b']

  # while loop to prevent image_filtered_inverted input error
  while True:
    # Choose type of filter based off invert filter
    image_filter_inverted = input("\nChoose: Negative: 'A' or Monochrome: 'B': ").casefold()

    # If input found in choice list, accept
    if image_filter_inverted in image_filter_inverted_choices:
      break # exit loop
    
    # If input not found in choice list, reject input and try again
    elif image_filter_inverted != image_filter_inverted_choices:
      print(colored("\nError: Please try 'A' or 'B' from the choices above\n", 'red'))
      False

  # Begin code duration time
  initiate = datetime.now()
  # Call function
  invert_distort(display_algorithm, image_filter_inverted)
  # Store function in a new variable
  imageInvert = invert_distort(display_algorithm, image_filter_inverted)
  print("\nFinishing your image...") 
  # Save Image (create new image)
  imageInvert.save("InvertIMG.jpg")


""" Drawing Filter
| If statement for drawing filter:
| Based off input choice (also with sub-filter)
| choice, function drawing_filter() is called to apply
| appropriate filter. Input prevention error while
| loop is also included in drawing filter if statement.
| Once filter applied, final image is stored in imageDrawing
| variable and saved as 'DrawingIMG.jpg'.
| ------
| module 'datetime' is used below to track total time
| taken to execute filter application. Total time
| take is printed for user to see.

"""
# Function drawing_filter() if statement
if image_filter_main in image_filter_main_choices[1]:

  # Image Filter Drawing choices
  image_filter_drawing_choices = ['a', 'b']

  #while loop to prevent image_filter_drawing input error
  while True:
    # Choose type of filter based off drawing filter
    image_filter_drawing = input("\nChoose: Sketch: 'A' or Engraving: 'B': ").casefold()

    # If input found in choice list, accept
    if image_filter_drawing in image_filter_drawing_choices:
      break # exit loop
    
    # If inpit not found in choice list, reject input and try again
    elif image_filter_drawing != image_filter_drawing_choices:
      print(colored("\nError: Please try 'A' or 'B' from the choices above\n", 'red'))
      False

  # Begin code duration time
  initiate = datetime.now()
  # Call function
  drawing_filter(display_algorithm, image_filter_drawing)
  # Store function in a new variable
  imageDrawing = drawing_filter(display_algorithm, image_filter_drawing)
  print("\nFinishing your image...")
  # Save Image (create new image)
  imageDrawing.save("DrawingIMG.jpg")


""" Contrast Filter
| If statement for contrast filter:
| Based off input choice, function contrast_filter()
| is called to apply appropriate filter. Input prevention
| error while loop is also included in inverted filter if statement.
| Once filter applied, final image is stored in imageContrast
| variable and saved as 'ContrastIMG.jpg'.
| ------
| module 'datetime' is used below to track total time
| taken to execute filter application. Total time
| take is printed for user to see.

"""
# Function contrast_filter() if statement
if image_filter_main in image_filter_main_choices[2]:
  # Begin code duration time
  initiate = datetime.now()
  # Call function
  contrast_filter(display_algorithm)
  # Store function in a new variable
  imageContrast = contrast_filter(display_algorithm)
  print("\nFinishing your image...")
  # Save Image (create new image)
  imageContrast.save("ContrastIMG.jpg")


###                  ###
##   Code Execution   ##
##        Timer       ##
###                  ### 

""" Timer (Print)
| Duration to execute code is tracked and stored
| into the initiate and terminate variables. They 
| are then subtracted and printed to user to inform
| total duration to execute code. method datetime.now()
| from 'time' module is used to track time.
"""
# End code duration time
# Print total duration of code
terminate = datetime.now()
print('\nDuration to execute code: {}'.format(colored((terminate - initiate), 'blue')))




