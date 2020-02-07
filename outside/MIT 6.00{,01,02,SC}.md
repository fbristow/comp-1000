MIT 6.00
========

MIT publishes many materials for 6.00 free for public consumption on their Open
Courseware website.

The course is titled: "Introduction to Computer Science and Programming".

Course description:

> This subject is aimed at students with little or no programming experience. It
> aims to provide students with an understanding of the role computation can
> play in solving problems. It also aims to help students, regardless of their
> major, to feel justifiably confident of their ability to write small programs
> that allow them to accomplish useful goals. The class will use the Python
> programming language.

Sources of information
----------------------

* The MIT Open Courseware website for the course.

Course objectives
-----------------

1. Learning a language for expressing computations—Python
2. Learning about the process of writing and debugging a program
3. Learning about the process of moving from a problem statement to a
   computational formulation of a method for solving the problem
4. Learning a basic set of "recipes"—algorithms
5. Learning how to use simulations to shed light on problems that don't easily
   succumb to closed form solutions
6. Learning about how to use computational tools to help model and understand
   data

Learning outcomes
-----------------

### Unit 1

#### Introduction

* Compare and contrast declarative and imperative knowledge.
* Compare and contrast stored-program vs fixed-program computers.
* Define the terms "syntax", "static semantics", and "semantics", relating to
  computer programming languages.
* Give examples of the kinds of errors that might happen in a program.
* Compare and contrast the workflow for compiled vs interpreted languages.

#### Core elements of a computer

* Use an editor to write and run a simple program (basic input and output).
* Describe the properties of an object.
* Define the terms "type", "expression", "type conversion", "keyword".
* Compare and contrast "straight line program" and "branching program".
* Define the term "conditional".
* Write simple arithmetic expressions in a program.
* Write conditional statements in a program.
* List the scalar/primitive types that can be used in a Python program (`int`,
  `float`, `bool`, `None`, `str`).
* Identify expressions that will result in an error.
* Explain the difference between a "script" and an "interpreter".
* Declare and initialize a variable.
* Explain the purpose of a comment.
* Convert between `str` and number types.
* Use a simple conditional statement (`if`/`else`) in a program.
* Use the modulus operator in a program.
* Use a relational operator in a program (`==`, `!=`).
* Nest conditional statements within conditional statements.
* Explain how "good" indentation helps improve the readability of a program.
* Use a looping structure in a program.


#### Problem solving

* List possible outcomes for a program terminating (return/throw).
* Define the term "for loop".
* Prove that a loop is going to exit using a decrementing function.
* Define the term "exhaustive enumeration".
* Use exhaustive enumeration as a guess-and-check strategy in a program.
* Define the term "brute force".
* Use a `for` loop in a program.
* Use approximation in a program as a strategy for guess-and-check with floating
  point numbers.
* Translate a specification of a problem (e.g., "Find $y$ such that $y\times y=x
  \pm\epsilon$) into a program.
* Approximate the complexity of an algorithm.
* Describe the "bisection search" strategy.
* Write a program that implements the bisection search strategy.

#### Machine interpretation of a program

* Define the terms "decomposition" and "abstraction".
* Write and use a function that accepts 1 or more parameters and returns
  information.
* Debug a program by inspecting values.
* Justify why you would want to write functions.
* Explain how functions are related to the ideas of decomposition and
  abstraction.
* List the parts of a function (name, parameters, body).
* Write a function specification (function comment).
* Evaluate scoping rules on variables with the same name.
* List the order of operations when a function is called. (variable binding,
  scope creation)
* Use `assert` to implement principles of defensive programming.
* Draw a diagram representing creation of scopes when calling functions.
* Define the term "stack frame".
* Use built-in IDE tools to evaluate the state of an application by inspecting
  stack frames.
* Use a `for` loop to iterate over a sequence (`str`).
* Access individual elements in a sequence.
* Access subsequences of elements from a sequence (slicing in Python).
* Use string functions in Python.

#### Objects in Python

* Define the terms "mutability" and "cloning".
* Use sequence types in Python (lists, tuples; create, index, accumulate).
* Use associative arrays in Python (dictionary; create, access w/ key, access
  all keys, access values, remove values, test for presence of key).
* List the properties of sequence types (order, indexing im/mutability).
* Use list methods in Python.
* Describe references in terms of names of variables referring to a list,
  aliasing.
* Use side-effects to change a value in a function, pass-by-reference, aliasing.
* Compare and contrast assignment and mutation.
* Evaluate statements that create nested list structures.
* Compare and contrast sequence types and dictionaries in Python.
 
#### Recursion

* Define the terms "recursion", "recursive case"/"inductive case", "base case".
* Write a recursive function to solve well-known problems (Fibonacci,
  palindrome).
* Use loops, string types, conditional statements and lists to accumulate the
  words in a string separated by a space character.
* Define the term "Divide-and-conquer".
* List examples of solutions that apply the "Divide-and-conquer" strategy.
* Reduce a problem into smaller, recursive problems using a divide and conquer
  strategy.
* Identify the base case for a recursive problem.
* Compare and contrast recursion to iteration. (?)
* Given a recursive function, show the state of the function as it is evaluated.

#### Debugging

* Explain why computers use binary to represent information.
* Explain why floating point numbers should not be tested for equality with
  equality operators.
* Debug a program using print statements.
* Convert between binary and decimal.
* Explain the limitation of converting some fractional numbers to binary.
* Use default values for parameters in a function.
* Write a function to test for approximate equality between floating point
  numbers.
* Identify who is the source of a bug in your program (it's you).
* Systematically search for a bug in a program using print statements.
* Use the scientific method as a guide to debug a program (hypothesis, collect
  data using print statements).
* Explain why repeatability is important in the process of debugging/testing.
* Methodically test a program by finding small inputs that consistently do not
  work as expected.
* Write a test harness for a function.

#### Efficiency and Order of Growth

* Explain why efficiency is important.
* Name the notation used to state complexity.
* Explain why measuring time is not an appropriate way to measure complexity of
  an algorithm or its implementation.
* List the types of runtime complexity (best case, worst case, average case).
* Explain why the focus of complexity analysis is the worst case.
* Determine the worst case run time of a function or fragment of code.
* Explain why additive or multiplicative constants are ignored when measuring
  runtime complexity.
* Define "Big Oh notation".
* List examples of common worst-case complexities (O(1), O(n), O(logn), etc).
* Order a list of worst-case complexities from fastest to slowest.
* Use a helper function to call a recursive function.
* Use the `global` modifier in Python to refer to variables outside the scope of
  a block.

#### Memory and Search Methods


