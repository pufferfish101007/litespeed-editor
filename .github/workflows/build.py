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
