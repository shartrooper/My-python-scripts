## Counter the number of occurrences
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)    

## Cleaner display with Pretty print

import pprint

pprint.pprint(count)

