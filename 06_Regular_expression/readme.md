### P1 - Write a regular expression to search digits inside a string
<br>

Input:
```sh
'aksh012-git012'
```

Output:
```sh
['012', '012']
```
<br>

### P2 - Find the words with exactly 8 letters from paragraph using regex
<br>

Input:
```sh
'Hello, My name is Aksh Maradiya. i am from junagadh'
```

Output:
```sh
['Maradiya', 'junagadh']
```
<br>

### P3 - Find the numbers starting with 212 from a string.
<br>

Input:
```sh
'212000 aksh012-git 34021245 mak212 2129'
```

Output:
```sh
['212000', '2129']
```
<br>

### P4 -  Loop through the list and apply the regex to each element so that only items ending with a semicolon (;) are matched
<br>

Input:
```sh
 ['aksh12;','maradiya;','kshitij;:','prachi;']
```

Output:
```sh
aksh12;
maradiya;
prachi;
```
<br>

### P5 -  Write a regular expression to get only the part of the email before the "@" sign and include the "@" sign
<br>

Input:
```sh
['aksh@gmail.com','@gmail.com','@','prachi012@gm.com']
```

Output:
```sh
['aksh@']
['prachi012@']
```
<br>

### P6 - Replace all special characters with space using regex
<br>

Input:
```sh
'ak-sh@gmail.com?'
```

Output:
```sh
ak sh gmail com 
```
<br>

### P7 - Replace the space character that occurs after a word ending with a or r with a newline character
#### Sample input: area not a _a2_ roar took 22
#### Sample output:
#### area
#### not a
#### _a2_ roar
#### took 22
<br>

Input:
```sh
"area not a _a2_ roar took 22"
```

Output:
```sh
area 
not a 
_a2_ roar 
took 22
```
<br>

### P8 -  Split the given input string on one or more repeated sequences of cat using regex
#### Sample input: firecatlioncatcatcatbearcatcatparrot
#### Sample output: ['fire', 'lion', 'bear', 'parrot']
<br>

Input:
```sh
'firecatlioncatcatcatbearcatcatparrot'
```

Output:
```sh
['fire', 'lion', 'bear', 'parrot']
```
<br>

### P9 -  Filter all elements that contain a sequence of lowercase alphabets followed by - followed by digits.
#### They can be optionally surrounded by {{ and }}. Any partial match shouldn't be part of the output.
#### Sample input: ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
#### Sample output: ['{{apple-150}}', 'grape-87']
<br>

Input:
```sh
['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
```

Output:
```sh
['{{apple-150}}', 'grape-87']
```