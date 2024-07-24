import pathlib

# function to return the file extension
file_extension = pathlib.Path(__file__).suffix
print("File Extension: ", file_extension)
