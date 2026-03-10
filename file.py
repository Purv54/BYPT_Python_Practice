


# myfile = open("test.txt", "a")
# myfile.write("\nthis is a test file\nhiii\nyooo")

# myfile = open("test.txt", "r")
# content = myfile.read()
# print(content)

# myfile.seek(0) # move the file pointer back to the beginning of the file
# content = myfile.read()
# print(f"this is new read: {content}")
# print(myfile.readlines())

# myfile.close()

with open("test.txt","r") as myfile:
    content = myfile.read()
    print(content)

with open("test.txt", mode="w") as myfile:
    myfile.write("this is a new file")
