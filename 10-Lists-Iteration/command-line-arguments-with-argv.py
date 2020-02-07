# Run this in Terminal
import sys

print(sys.argv)
print(type(sys.argv))

word_lengths = 0

for arg in sys.argv[1:]:  # index 0 = filename
    word_lengths += len(arg)
print(f"the total length if all command-line arguments is {word_lengths}")



