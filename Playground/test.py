import re

import re

s = 'geeks.forgeeks'

# without using \
match = re.search('.', s)
print(match)
print('Start Index:', match.start())
print('End Index:', match.end())

# using \
match = re.search('\.', s)
print(match)

print('Start Index:', match.start())
print('End Index:', match.end())

