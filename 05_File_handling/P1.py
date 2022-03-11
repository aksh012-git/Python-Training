# You have two files named questions.txt and answer.txt. You need to create a file that contains questions and answers. But both input files contain random questions followed by a numeric value. You need to match both values and then copy the question-answer pair in a new file.
# -> Optimize code properly.
# Sample file: question.txt:
# 3. What is your Hobby?
# 1. What is your name?
# 2. Where are you from?
# Sample file: answer.txt:
# 	2. India
# 	1. Bob
# 	3. Swimming
# Output file:
# 1. What is your name?
# Bob
# 2. Where are you from?
# 	India
# 	3. What is your Hobby?
# 	Swimming
 

que_file = open('questions.txt')
ans_file = open('answer.txt')

que_ans_joint = que_file.read() +'\n'+ ans_file.read()
list_of_que_ans = que_ans_joint.splitlines()
list_of_que_ans.sort(key = lambda value_of_list:int(value_of_list[0]))

question_answer = open('question-answer.txt','w')
for i in list_of_que_ans:
    question_answer.write(i+'\n')
question_answer.close()
    



            
    