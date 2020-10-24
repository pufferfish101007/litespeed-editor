import os

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = [] # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("src")

filename = "README.md"
with open(filename, 'w') as file_object: # open file function with 'w' argument to allows write some text
    print('File has been opened successfully!\n') # if file successfully opened, this program will be shown
    text = 'Text that you want to add' # if file has been successfully opened. 
    # it will be allowed user to input some text
    file_object.write(text) # write function to write text to file

# make sure that we have successfully add some text inside that file with read function
with open(filename) as read_object: # again, we open the file
    content = read_object.read() # read function to check wheter there is any text inside that file

if text in content: # check wheter text already added successfully.
    print('You have been successfully to add text to your file!') # if text successfully added. print text!
    print('Your text : ' + text)
