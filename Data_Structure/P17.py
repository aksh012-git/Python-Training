# Print reverse string using recursion
# A = "helloworld"
# ans = "dlrowolleh"

def reverse_string(string,ending_index):
    ending_index -= 1
    if ending_index == 0:
        return string[ending_index]
    return string[ending_index] + reverse_string(string,ending_index)

string = "helloworld"
print(reverse_string(string,len(string)))
    
    