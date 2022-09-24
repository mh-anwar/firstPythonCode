from sys import argv
from os.path import exists
script = argv[0]
from_file = argv[1]
to_file = argv[2]
print(f"Copying from {from_file} to {to_file}")


in_data = open(from_file).read()

print(f"THe input file is {len(in_data)} bytes long")

print(f"Does the output file exist?{exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(in_data)

print("Alright, all done.")
