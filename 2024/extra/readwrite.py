# using os / terminal through code
import os

# get current working directory
current_directory = os.getcwd()
print(current_directory)



# modes:
# a = append
# w = write
# r = reads that file

# wusing with open with mode "a"
# with open("demo.txt", "a") as file:
#     file.write("Hello world\n")

# using with open with mode "w"
with open("demo.txt", "w") as file:
    file.write("Hello world\n")

file_path = current_directory + "\demo.txt"
if os.path.exists(file_path):
    # using with open mode "r"
    with open("demo.txt", "r") as file:
        contents = file.read()
        print(contents)    
else:
    print("file doesnt exist")

# make 1 file called questions.txt
# 1x1=
# 1x2=
    
    