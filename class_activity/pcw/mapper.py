import sys

# Read lines from standard input
for line in sys.stdin:
    # Strip leading/trailing whitespace and split the line into words
    words = line.strip().split()

    # Emit a key-value pair for each word
    # The key is the word, the value is 1
    # Hadoop Streaming uses tab as the default separator
    for word in words:
        print(f'{word}\t1')