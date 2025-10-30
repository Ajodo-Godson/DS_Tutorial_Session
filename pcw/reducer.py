import sys

current_word = None
current_count = 0

# Read key-value pairs from standard input (output of mapper)
for line in sys.stdin:
    # Split the line into word and count
    word, count = line.strip().split('\t', 1)

    # Convert count to an integer
    try:
        count = int(count)
    except ValueError:
        # Ignore lines where the count is not a number
        continue

    # Hadoop sorts the mapper output by key.
    # So, we'll see all pairs for a given word together.
    if current_word == word:
        current_count += count
    else:
        # A new word has started. If current_word is not None,
        # print the count for the previous word.
        if current_word:
            print(f'{current_word}\t{current_count}')
        
        # Reset for the new word
        current_word = word
        current_count = count

# IMPORTANT: Output the last word's count after the loop ends
if current_word:
    print(f'{current_word}\t{current_count}')