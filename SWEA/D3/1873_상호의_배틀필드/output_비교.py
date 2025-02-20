import difflib

with open("output1.txt", "r") as f1, open("output.txt", "r") as f2:
    diff = difflib.unified_diff(f1.readlines(), f2.readlines(), lineterm="")

for line in diff:
    print(line)