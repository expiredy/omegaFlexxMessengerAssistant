import _csv
import csv
import shutil
import sys

files_for_parsing = ["positive.csv", "negative.csv"]

maxInt = sys.maxsize

while len(str(maxInt)) > 2:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
print(maxInt)
for file_name in files_for_parsing:
    with open(file_name, encoding="windows-1251", newline='', errors='ignore') as csvfile:
        # shutil.copyfileobj(csvfile, sys.stdout)
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        with open(file_name.replace(".csv", ".txt"), mode="a") as new_file:
            print(reader.line_num)
            try:
                for line in reader:
                    try:
                        new_file.write(str(line))
                    except BaseException:
                        pass
            except _csv.Error:
                pass
    print(file_name + " is done")