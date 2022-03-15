### Take the word and its meaning as input from the user.
#### -> Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
#### -> Now use the __str__() function to return a string that contains the word and meaning.
#### -> Store the returned strings in a list named flash.
#### -> Use a while loop to print all the stored flashcards.
#### -> Add proper error handling
#### -> Result image is attached in thread
<br>

Input: 
```sh
Enter word: k
Enter meaning of entered word: oky
```
Output:
```sh 
k ( oky )
```

### Create classes according to the following class map:
#### ->  Animal => Wild => Leopard, Tiger
#### 	=> Pet => Dog
#### 	=> Canine => Fox
#### -> Each class contains two methods to get a name and info. Get the name returns the name of that animal and get the info returns hierarchy.
#### For example,
#### print(dog.get_name())  ⇒ My name is Tommy
#### print(dog.get_info())  ⇒  I am Dog. I am Pet. I am Animal

Input: 
```sh
Create object of any class 
call method 
```
Output:
```sh 
prints statement inside the class method and parent class method.
```

###  Create class Cards with two list suits (Hearts, Diamonds, Clubs, Spades) and  values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
#### -> Create a class deck. That contains a method to get a card set containing 52 elements.
#### -> Create class shuffle. That contains two methods to shuffle given cards and remove/pick a single card.
#### -> Create two objects of the above class as players. Each player pick/remove 5 cards from the shuffle cards. Total points of both players and display name of winner player.

Input: 
```sh
Create object of playes 
```
Output:
```sh 
print points of players and winner player name
```

### Create a class for Users,
#### username
#### account no
#### mobile no
#### address
#### account balance
### -> Create a class for user manager
#### Manages user => Add new user, Get existing user, remove user
### -> Create a class for ATM,
#### Enter account no and get user if not found then show a valid message
### Show options for user operations like creating new users, View Balance. Deposit, Withdraw, Close account, etc...
#### Transaction charge: 0.5 for every operation
#### Account balance limit: 10000 
<br>

Input & Output: 
```sh
Welcome to India Bank

Enter : 0, User Module
Enter : 1, Admin user
Enter : 2, Quit
0

Enter 0: Enter Account no
Enter 1: create new account
Enter 2: back
1
Enter Your Name: aksh
Enter Your mobile no: 9712891011
Enter Your adrress: mvr
Enter the amount of balance that you want to deposit.
Account balance limit: 10000
:)10000
Congratulations 🥳, Now you are member of India bank
Please note your Account no 1111

Enter 0: Enter Account no
Enter 1: create new account
Enter 2: back
0
Enter account no: 1111

Enter 0:Show Account Details
Enter 1: Deposit
Enter 2:Withdraw
Enter 3:Close account
Enter 4:Back
:1
Enter amount: 2000
Now your current balance is 12000

Enter 0:Show Account Details
Enter 1: Deposit
Enter 2:Withdraw
Enter 3:Close account
Enter 4:Back
:4

Enter 0: Enter Account no
Enter 1: create new account
Enter 2: back
2

Enter : 0, User Module
Enter : 1, Admin user
Enter : 2, Quit
2
```

### Create class Person:
#### Name
#### DOB
#### City
#### Contact No
### Create class Employee (Inherit person class)
#### employee id
#### joining date
#### salary
#### department
#### post
### Employee manager class
#### Add/Remove Employee, Get all employees list, get employee by his name, get all employees by his/her department,
#### Task:
#### Add few employees
#### Print all the employees
#### Find an employee with the name
#### Print all employees with department Finance
#### Find all employees whose salary is greater than 50000
#### Find all employees whose salary is between 50000-100000
#### Find a list of employees who are joined in the current year
#### Find all employees who are from Mirzapur
#### Find employees whose birthday in the current month
#### Sort employee list with salary in descending order
<br>

Input & Output:
```sh

|                                                      |
|--------------- Weboccult Technologies ---------------|
|                                                      |

Enter 0: Add new Employee
Enter 1: See all Employees
Enter 2: Search
Enter 3: Remove user
Enter 4: Quit
:)0

Enter name: aksh
12/08/2001
mvr
9712891011
01/01/2022
20000
aiEnter Date of birth (in DD/MM/YYYY): /ml
traineeEnter city: Enter Contact No.: Enter Joining date (in DD/MM/YYYY): Enter salary: Enter Department: Enter post: 

--------- Generated employee id for [aksh] is [1111] ----------

Enter 0: Add new Employee
Enter 1: See all Employees
Enter 2: Search
Enter 3: Remove user
Enter 4: Quit
:)1

Employee id: [1111] Name: [aksh] Date of birth: [2001-08-12] City: [mvr] Contact No.: [9712891011] Joining date: [2022-01-01] Salary: [20000] Department: [ai/ml] Post: [trainee]

Enter 0: Add new Employee
Enter 1: See all Employees
Enter 2: Search
Enter 3: Remove user
Enter 4: Quit
:)2

Enter 0: Search by Name|City|Employee Id|Contact No|Department|Post
Enter 1: Search by salary
Enter 2: Search by Joining Year
Enter 3: See Employee's birthday in current month
Enter 4: back
:)0
Search by Name|City|Employee Id|Contact No|Department|Post
:)mvr
Employee id: [1111] Name: [aksh] Date of birth: [2001-08-12] City: [mvr] Contact No.: [9712891011] Joining date: [2022-01-01] Salary: [20000] Department: [ai/ml] Post: [trainee]

Enter 0: Search by Name|City|Employee Id|Contact No|Department|Post
Enter 1: Search by salary
Enter 2: Search by Joining Year
Enter 3: See Employee's birthday in current month
Enter 4: back
:)4
Enter 0: Add new Employee
Enter 1: See all Employees
Enter 2: Search
Enter 3: Remove user
Enter 4: Quit
:)4

```