# Python script to post-process svg files
# Problem: pdf was read in as svg. In shapes from pdf, many contain styling
#          determined by icc-color(sRGB-IEC61966-2, 0.1, 0.99598694, 0.83898926, 0)
#          In other viewers (e.g., Figma) and in web, this causes incorrect rendering
#          either as a black shape or missing.
# Fix: This script will search the svg file for that text and remove it. Note, I checked by finding
#      and replacing all occurences that matched icc-color\(.*\) using Sublime. Now implement
#      in Python for good practice and ease of replication in the future.
# Resources
#  https://stackoverflow.com/questions/43872978/search-and-alter-text-with-python-in-a-svg-file
#  https://stackoverflow.com/questions/67694024/how-to-modify-the-contents-of-an-svg-file-with-python
#  https://pythonexamples.org/python-replace-string-in-file/
# Attempt 1:
#      Worked when I changed it in Sublime, but not Python. Searched for icc-color and didn't show up
#      Try again with the exact same file. Ah I think I forgot to change the output from data to fixed!
#      Looks like it is working now!
import os
import re # for regex
os.getcwd()

# open and read in the svg as text
fin = open("project/static/images/edited_runs_3_export_small.svg", "rt")
data = fin.read()

# replace all occurrences of the required string
fixed = re.sub("icc-color\\(.*\\)", "", data)

# close the input file
fin.close()

# open the input file in write mode
fin = open("project/static/images/edited_runs_3_export_small_fixed.svg", "wt")

#overrite the input file with the resulting data
fin.write(fixed)

#close the file
fin.close()
