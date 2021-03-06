-   Make a variable called “number of dots” and set its value to the input
    entered by the end user.
    Make another variable called “cards”.
    Below is the algorithm to help you program this:

```
If “number of dots” less than or equal to 31
  If “number of dots” greater than or equal to 16
    Subtract 16 from “number of dots” and add “16, ” to string variable “cards”
  If “number of dots” greater than or equal to 8
    Subtract 8 from “number of dots” and add “8, ” to string variable “cards”
  If “number of dots” greater than or equal to 4
    Subtract 4 from “number of dots” and add “4, ” to string variable “cards”
  If “number of dots” greater than or equal to 2
    Subtract 2 from “number of dots” and add “2, ” to string variable “cards”
  If “number of dots” greater than or equal to 1
    Subtract 1 from “number of dots” and add “1, ” to string variable “cards”
  Display the value of “cards”
else
  Ask the end user to enter a number less than or equal to “31”
```

-   The `scratch:if <> then` block checks if the condition is true and then
    runs the blocks inside of the IF block.
    In this challenge you need to use `scratch:if <> then` blocks to check if
    the “number of dots” is greater than or equal to 16 (use the
    `scratch:<> or <>` block under “Operators”).
    If it is, display card “16” and subtract 16 from your number and do the
    same with the rest of the cards.
-   You can also use the IF THEN ELSE block (see image below) if you need to run
    a set of blocks if the condition is not true.

```scratch
if <> then
else
end
```

-   In the extra challenge you need to ask the user to enter a number less
    than or equal to 31 if the input which was entered was greater than 31.
-   Test your program with some values on the boundaries (i.e. 32, 31, 16, 8,
    4, 2, 1)
