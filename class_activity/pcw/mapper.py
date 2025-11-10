import sys

# Read lines from standard input
for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        # Python 2 string formatting
        print('%s\t1' % word)
