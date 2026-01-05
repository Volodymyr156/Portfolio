# #1
import os
import sys
# usrargs = sys.argv
#
# if len(usrargs) != 2:
#     print("Usage: python HW26.py <dir>")
#     sys.exit(1)
#
# path = usrargs[1]
# if not os.path.isdir(path):
#     print(f"Error: {path} is not a directory")
#     sys.exit(1)
#
# print(f"Elements of directory: {path}")
#
# print("List of files:")
# for el in os.listdir(path):
#     if os.path.isfile(os.path.join(path, el)):
#         print(f"file - {el}")
#
# print("List of directories:")
# for d in os.listdir(path):
#     if os.path.isdir(os.path.join(path,d)):
#         print(f"dir - {d}")

#2
newargs = sys.argv
usr_path = newargs[1]
ext = newargs[2]
list_of_files = []

if len(newargs) < 2:
    print("Usage: python HW26.py <dir> <extension>")
    sys.exit(1)

if not os.path.isdir(usr_path):
    print(f"Error: {usr_path} is not a directory")
    sys.exit(1)

print("List of found files:")
for root,_, files in os.walk(usr_path):
    for file in files:
        if file.endswith(ext):
            list_of_files.append(os.path.join(root, file))
            print("-",os.path.join(root, file))


verdict = input("Victims found. Awaiting for execution... (y/n): ")

while True:
    if verdict == "y":
        print(f"Chainsaw turned on...")
        for v in list_of_files:
            os.remove(v)
        print("Successfully removed all files")
        break
    if verdict == "n":
        print("Well...okay")
        break
    else:
        verdict = input("Incorrect answer (y/n): ")


