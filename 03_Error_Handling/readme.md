### p1 - You're going to write an interactive calculator!
#### User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space
#### (e.g. 1 + --> Split user input and check whether the resulting list is valid:
#### -> If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#### -> Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
#### -> If the second input is not '+' or '-', again raise a FormulaError
#### -> If the input is valid, perform the calculation and print out the result.
#### -> The user is then prompted to provide new input, and so on until the user enters quit.
#### -> Example image in attached in thread
<br>

Input: Input as a string which includes space-separated number and operation split space-separated and converts into a list<br>
Output: Output as sum summation/subtraction of 2 integer value in the string if the input is not proper format then ran custom exception <br><br>

| Input | Output |
| ----- | ----- |
| 1 + 2 | 3 |
| 1.4 + 2.6 | 4 |
| a + 2 | handling exception |
| quit | program stopped |

#

### P2 - Create while loop which increase counter by one every second.
#### -> Start count from 0
#### -> Stop while loop when counter is grater than 500
#### -> Program must not stop on any keyboard press. (Not even ctrl + c or ctrl + x)
<br>

Input: Input as variable = 0<br>
Output: print 0 to 500 

| Input | Output |
| ----- | ----- |
| x = 0 | 0 |
|  | . |
| | . |
|  | . |
| | . |
|  | . |
| | . |
|  | 500 |
#