import sys

current_word = None
current_count = 0

# Read key-value pairs from standard input (output of mapper)
for line in sys.stdin:
    parts = line.strip().split('\t', 1)
    if len(parts) != 2:
        continue
    word, count = parts

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%d' % (current_word, current_count))
        current_word = word
        current_count = count

# Output the last word's count
if current_word:
    print('%s\t%d' % (current_word, current_count))
