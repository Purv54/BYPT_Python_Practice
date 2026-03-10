f = open("file1.txt", "w")
f.write("this is file one")
f.close()

f = open("file2.txt", "w")
f.write("this is file two")
f.close()

import zipfile

com_file = zipfile.ZipFile("compressed.zip", "w")
com_file.write("file1.txt", compress_type=zipfile.ZIP_DEFLATED)
com_file.write("file2.txt", compress_type=zipfile.ZIP_DEFLATED)
com_file.close()

zip_obj = zipfile.ZipFile("compressed.zip", "r")
zip_obj.extractall("extracted")
zip_obj.close()
# The zipfile module provides tools to create, read, write, append, and list archives in ZIP format. 
# The ZipFile class is used to work with ZIP files. 
# To create a ZIP file, you can use the ZipFile constructor with the mode 'w' for writing. 
# The write() method is used to add files to the ZIP archive. 
# The compress_type argument specifies the compression method to be used. 
# To extract files from a ZIP archive, you can use the ZipFile constructor with the mode 'r' for reading. 
# The extractall() method is used to extract all the contents of the ZIP archive to a specified directory. 
# The close() method is used to close the ZIP file after you are done working with it.      
