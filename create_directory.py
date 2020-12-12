# Quick script to create the folder and files needed for a new day

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-y", help="Put the year for the folder: int", type=int)
parser.add_argument('-d', help="Put the day for the inner folder and files: int", type=int)
args = parser.parse_args()

day = args.d
year = args.y

path = os.getcwd()
new_path = "{}\{}".format(path, year)

# Make Folder
try:
    if os.path.isdir(new_path):
        pass
    else:
        os.mkdir(new_path)
except:
    print("Failure Making New Directory")
    exit(1)

day_path = "{}\day{}".format(new_path, day)
# Make day directory
try:
    if os.path.isdir(day_path):
        pass
    else:
        os.mkdir(day_path)
except:
    print("Failure making day directory")
    exit(1)


# Make Files
try:
    if os.path.isfile("{}\{}".format(day_path, "day{}.py".format(day))):
        pass
    else:
        open("{}\day{}\day{}.py".format(year, day, day), "x")

    if os.path.isfile("{}\{}".format(day_path, "day{}_2.py".format(day))):
        pass
    else:
        open("{}\day{}\day{}_2.py".format(year, day, day), "x")

    if os.path.isfile("{}\{}".format(day_path, "day{}Input.txt".format(day))):
        pass
    else:
        open("{}\day{}\day{}Input.txt".format(year, day, day), "x")
except:
    print("Failure making Files")
    exit(1)    

print("Success")