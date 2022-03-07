# Split the given input string on one or more repeated sequences of cat using regex
# Sample input: firecatlioncatcatcatbearcatcatparrot
# Sample output: ['fire', 'lion', 'bear', 'parrot']

import re
import re

s_nums = 'firecatlioncatcatcatbearcatcatparrot'
lst = re.split('(?:cat)+', s_nums)
print(lst)


# >>> re.findall('(?:aa)+', 'aa')
# ['aa']
# >>> re.findall('(?:aa)+', 'aaaa')
# ['aaaa']
# >>> re.findall('(?:aa)+', 'aaaaa')
# ['aaaa']