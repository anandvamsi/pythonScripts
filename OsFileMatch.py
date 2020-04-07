import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "*.py"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (entry)
