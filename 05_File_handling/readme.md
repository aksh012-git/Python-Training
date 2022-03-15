### You have two files named questions.txt and answer.txt. You need to create a file that contains questions and answers. But both input files contain random questions followed by a numeric value. You need to match both values and then copy the question-answer pair in a new file.
<br>

#### -> Optimize code properly.
#### Sample file: question.txt:
#### 3. What is your Hobby?
#### 1. What is your name?
#### 2. Where are you from?
#### Sample file: answer.txt:
#### 	2. India
#### 	1. Bob
#### 	3. Swimming
#### Output file:
#### 1. What is your name?
#### Bob
#### 2. Where are you from?
#### 	India
#### 	3. What is your Hobby?
#### 	Swimming

<br>

Input Files:

```sh
=> Questions.txt: 

3. What is your Hobby?
1. What is your name?
2. Where are you from?
```


```sh
=> Answer.txt:

2. India
1. Bob
3. Swimming
```
Output Files:
```sh
=> question-answer.txt

1. What is your name?
1. Bob
2. Where are you from?
2. India
3. What is your Hobby?
3. Swimming
```