#  Filter all elements that contain a sequence of lowercase alphabets followed by - followed by digits.
# They can be optionally surrounded by {{ and }}. Any partial match shouldn't be part of the output.
# Sample input: ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
# Sample output: ['{{apple-150}}', 'grape-87']

import re

lst_input =  ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
lst_output = []

for item in lst_input:
    if re.match('{{+[a-z]+\-+[0-9]+}}|[a-z]+\-+[0-9]+',item):
        lst_output.append(item)

print(lst_output)