
'''
Decription of move_to_folder:
final_directory is the folder which the category folders are under and needs to be a string
It should not be a problem if there is not already a pre-existing text file for each class.
It creates one automatically if one does not exist and adds on if one does exist
'''

def move_to_folder(old_image_path, final_directory, categorized_as):
    import os
    image_basename = (os.path.basename(old_image_path))
    directory = final_directory + "/" + categorized_as
    if os.path.exists(directory) == False:
        print "Error: the training folder does not exist so a new one was made"
    new_path = (directory + "/" + image_basename)
    print ( "The new image path is " + new_path)
    while os.path.exists(new_path) == True:
        filename, file_extension = os.path.splitext(new_path)
        new_path = (filename + "(0)" + file_extension)
        print (new_path)
        return new_path
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.rename(old_image_path, new_path)
    print ("image moved to " + new_path)