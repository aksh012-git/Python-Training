que_file = open('questions.txt')
ans_file = open('answer.txt')

que_ans_joint = que_file.read() +'\n'+ ans_file.read()
list_of_que_ans = que_ans_joint.splitlines()
list_of_que_ans.sort(key = lambda value_of_list:int(value_of_list[0]))

question_answer = open('question-answer.txt','w')
for i in list_of_que_ans:
    question_answer.write(i+'\n')
question_answer.close()
    



            
    