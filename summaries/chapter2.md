# Chapter 2: Flow Control.

## Summaries what i learned in this chapter.
- Boolean Values
- Comparison Operators
- Boolean Operators: 1. Binary Boolean Operators | 2. The not Operator
- Flow Control Statement: if, else and elif
- While Loop Statements and also learned An annoying while loop
- Break Statement and Continue Statement
- Loop and the range() Function
- Importing Modules: ramdom, sys( sys.exit() )

## QUESTIONS
- [Question](../images/ch2_practice.png)

### ANSWERS
1. Boolean data type has only two values: True and False.
2. the three Boolean operators: and, or and not.
3. - The and Operator's Truth Table:
     - True and True = True
     - True and False = False
     - False and True = False
     - False and False = False
  - The or Operator's Truth Table:
     - True or True = True
     - True  or False = True
     - False or True = true
     - False or False = False
  - The not Operator's Truth Table:
     - not True = False
     - not False = True
4. The following expessions evaluate to:
   - (5 > 4) and (3 == 5) -> False
   - not (5 > 4) or (3 == 5) -> False
   - not (5 > 4) -> False
   - (5 > 4) or (3 == 5) -> True
   - (True and True) and (True == False) -> False
   - (not False) or (not True) -> True
5. The six comparison operators:
     - ==
     - !=
     - =>
     - =>
     - >
     - <
6. The difference between the equal to opeerator(==) and the assingment operator(=):
    - The == operator (equal to) asks whether two volues are the same as each other.
    - The = operator (assingment) puts the volue on the right into the variable on the         left.
7.  - A condition is an expression that evaluates to a Boolean value, which is either          True or False.
    - I would use a condition in control flow statements, such as if statements or           while loops, to decide whether a specific block of code should be executed.
8. Identify the three blocks in code:
    - if spem == 10:
    - if spam > 5:
    - else:
9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in      spam, and prints Greetings! if anything else is stored in spam:
        if spem == 1:
           print("Hello")
        fi spen == 2:
          print("Howdy")
        else:
          print("Greetings!")
10. If my program is stuck in an infinite loop I can press Ctrl + c
11. The difference between break and continue
    - break immediately terminates the loop entirely and moves execution to the code           right after the loop.
    - continue immediately stops the current iteration of the loop and jumps back to the       top of the loop to check the condition for the next iteration.
12. the difference between range(10), range(0, 10), and range(0, 10, 1)in a for loop:
    - range(10): Takes one argument (stop). It starts at 0 and increments by 1 by              default.
    - range(0, 10): Takes two arguments (start, stop). It explicitly states to start at         0.
    - range(0, 10, 1): Takes three arguments (start, stop, step). It explicitly states       to start at 0 and increase by 1 on each iteration.
13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write       an equivalent program that prints the numbers 1 to 10 using a while loop.
    for:
         for i in range(1,11):
         print(i)
    while:
         i = 1
         while i <= 10:
           print(i)
           i = i + 1
14. I world cell: spem.bacon()         

   
    
     

