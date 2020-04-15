Course prerequisites {.unnumbered}
====================

Before entering this course, a student should be able to:

-   Evaluate arithmetic expressions, applying the rules of order of
    operation to basic arithmetic operators (+, −, ×, ÷).
-   Use trigonometric functions to calculate angles.
-   Download and install software on a computer.

Importantly: students are **not** expected to have any previous
programming experience.

Course outcomes {.unnumbered}
===============

By the end of this course, a student should be able to:

1.  [Write and run moderately complex programs using a procedural
    programming language.]{tags=":program:"}
2.  [Read and evaluate written programs.]{tags=":evaluate:"}
3.  [Describe basic programming concepts and structures in plain
    English.]{tags=":communicate:"}
4.  [Represent ideas and information in a way that computers can
    understand and act on.]{tags=":represent:"}
5.  [Analyze and implement basic searching
    algorithms.]{tags=":algorithms:"}

Learning objectives {.unnumbered}
===================

```{=tex}
\setcounter{section}{1010}
```
Programming Basics
------------------

By the end of this unit, students should be able to:

1.  [Use an integrated development environment (IDE) to write and run a
    simple, linear program using a procedural programming
    language.]{tags=":program:"}
    1.  Use *literal values* in a program.
    2.  Describe what code does using *comments*.

IDE
:   Software that simplifies writing software in a *specific*
    programming language.

Examples of IDEs:

(1) [Processing] is an IDE for writing software in the Processing
    programming language.
(2) [DrJava] is an IDE for writing software in the Java programming
    language.
(3) [Spyder] is an IDE for writing software in the Python programming
    language.

  [Processing]: https://processing.org/
  [DrJava]: http://drjava.org/
  [Spyder]: https://www.spyder-ide.org/

### Programming Basics: Processing

By the end of this unit, students should be able to:

1.  [Draw points, lines, and shapes on the Processing
    canvas.]{tags=":program:"}
2.  [Change properties of shapes and the canvas, like background colour,
    outline colour, fill colour, size, position, and line
    weight.]{tags=":program:"}

Variables and Integers
----------------------

By the end of this unit, students should be able to:

1.  [Declare and use a variable in a program to represent
    information.]{tags=":represent: :program:"}
    1.  Initialize a variable using a literal value.
2.  [Write and evaluate arithmetic expressions (+, −, ×, ÷, mod) that
    include both literal values and
    variables.]{tags=":program: :evaluate:"}
3.  [Explain the purpose of the modulus operator.]{tags=":communicate:"}
    1.  List uses of the modulus operator.
4.  [Debug simple errors by inspecting the value of a variable as the
    program is running.]{tags=":program:"}
5.  [Identify compile-time errors in a fragment of code (e.g., incorrect
    case on function names, duplicated variable names, non-existent
    variables).]{tags=":evaluate:"}

Coding Style and Standards
--------------------------

By the end of this unit, students should be able to:

1.  [Choose meaningful variable names that make code more
    readable.]{tags=":communicate:"}
2.  [Declare and use *named constants* in a program.]{tags=":program:"}
3.  [Identify values that should be represented as a named
    constant.]{tags=":represent:"}
4.  [Explain how named constants can be used as a safety
    feature.]{tags=":communicate:"}
5.  [Compare and contrast named constants and regular
    variables.]{tags=":communicate:"}

Active Programs
---------------

By the end of this unit, students should be able to:

1.  [Use a "global variable" in a program to maintain
    state.]{tags=":program:"}
    1.  [Represent application state in a variable.]{tags=":represent:"}
2.  [Write a program that accepts and reacts to input from a
    user.]{tags=":program:"}

### Active Programs: Processing

By the end of this unit, students should be able to:

1.  [Use the global variables exposed in the Processing environment as
    input to a program, like mouse position ([`mouseX`] and
    [`mouseY`]).]{tags=":program:"}
2.  [Write a program that changes the canvas as time
    passes.]{tags=":program:"}
3.  [List the special function names that are used in
    Processing.]{tags=":communicate:"}
4.  [Order the function names by when they are executed when a
    Processing program is started.]{tags=":communicate:"}
5.  [Explain the purpose of each of the special function names used in
    Processing.]{tags=":communicate:"}

  [`mouseX`]: https://processing.org/reference/mouseX.html
  [`mouseY`]: https://processing.org/reference/mouseY.html

User-defined Functions, part 1
------------------------------

By the end of this unit, students should be able to:

1.  [Create and use user-defined functions that accept no inputs and do
    not `return` any data, in a program.]{tags=":program:"}
    1.  Choose a concise and meaningful name for a user-defined
        function.
2.  [Identify a syntactically correct function signature from a list of
    function signatures.]{tags=":evaluate:"}
3.  [Trace the execution of code when user-defined functions are
    called.]{tags=":evaluate:"}
4.  [Define the term "local variable".]{tags=":communicate:"}
5.  [Determine the visibility of a variable declared in a
    program.]{tags=":evaluate:"}
6.  [Define the term "scope" in terms of variable visibility when
    declared within a function.]{tags=":communicate:"}
7.  [Compare and contrast local and global
    variables.]{tags=":communicate:"}

Real Numbers - `float`s
-----------------------

By the end of this unit, students should be able to:

1.  [Declare and use floating-point-type variables in a
    program.]{tags=":program:"}
2.  [Evaluate an expression containing floating point
    numbers.]{tags=":evaluate:"}
3.  [Determine the type of the result of evaluating an
    expression.]{tags=":evaluate:"}
4.  [Use compound assignment/arithmetic operators (e.g., `+=`,
    `++`).]{tags=":program:"}
5.  [Explain the difference between integers and real
    numbers.]{tags=":communicate:"}
6.  [Explain how and why floating point numbers are limited when being
    represented in binary by a computer.]{tags=":communicate:"}
7.  [Use language libraries for evaluating trigonometric or other math
    functions.]{tags=":program:"}

### Real Numbers - `float`s: Processing

By the end of this unit, students should be able to:

1.  [Use the canvas size to change the behaviour of a program
    ([`width`], [`height`]).]{tags=":program:"}

  [`width`]: https://processing.org/reference/width.html
  [`height`]: https://processing.org/reference/height.html

Text and Strings
----------------

By the end of this unit, students should be able to:

1.  [Create and use `String`-type variables in a
    program.]{tags=":program:"}
    1.  Combine multiple `String`s together using the concatenation
        operator.
    2.  Call an instance method on a `String` to get its length.
    3.  Access individual characters in a `String`, by *index*.
2.  [Convert between number types and `String` types.]{tags=":program:"}
3.  [Explain why number types cannot be assigned to `String` types, and
    vice-versa.]{tags=":communicate:"}
4.  [Create and use a `char`-type variable in a
    program.]{tags=":program:"}
5.  [Evaluate expressions that operate on `String`s.]{tags=":evaluate:"}
    1.  Calling instance methods.
    2.  Concatenation operator.
    3.  Order of operations (e.g., `"hello" + (10 + 2)`).

### Text and Strings: Processing

By the end of this unit, students should be able to:

1.  [Draw text on the canvas.]{tags=":program:"}

Data Types and Memory
---------------------

By the end of this unit, students should be able to:

1.  [Use different number types to represent numbers (e.g., `double`,
    `float`, `long`, `int`, `short`).]{tags=":program:"}
2.  [Choose a specific number type to represent a value, minimizing
    required memory.]{tags=":represent:"}
3.  [Convert between number types using explicit and implicit
    casts.]{tags=":program:"}
4.  [Evaluate an expression containing implicit and explicit
    casts.]{tags=":evaluate:"}
5.  [Explain what happens to a numeric value when explicit down-casting
    is applied.]{tags=":communicate:"}
6.  [Define the term "Integer overflow".]{tags=":communicate:"}

True and False - Booleans
-------------------------

By the end of this unit, students should be able to:

1.  [Declare and use `boolean` variables in a
    program.]{tags=":program:"}
2.  [Evaluate `boolean` expressions with logical operators (e.g., `and`,
    `or`, `not`).]{tags=":evaluate:"}
3.  [Use conditional statements (`if` and `else`) in a
    program.]{tags=":program:"}
    1.  Use *nested* conditional statements in a program.
4.  [Decide if a variable is visible (scope) in a nested
    block.]{tags=":evaluate:"}

### True and False - Booleans: Processing

By the end of this unit, students should be able to:

1.  [Use keyboard and mouse state (keys pressed or not) to affect the
    behaviour of a program ([`mousePressed`],
    [`keyPressed`]).]{tags=":program:"}

  [`mousePressed`]: https://processing.org/reference/mousePressed.html
  [`keyPressed`]: https://processing.org/reference/keyPressed.html

Advanced Conditionals
---------------------

By the end of this unit, students should be able to:

1.  [Use relational operators to compare number types in a program
    (e.g., `>`, `<`, `>=`, `<=`, `==`, etc).]{tags=":program:"}
2.  [Evaluate Boolean expressions containing both logical and relational
    operators.]{tags=":evaluate:"}
3.  [Call an instance method on a `String` to *compare* it to another
    instance of `String`.]{tags=":program:"}
4.  [Write *concise* logical expressions (i.e., write `if(x)`, **not**
    `if(x==true)`).]{tags=":program:"}
5.  [Explain why floating-point numbers cannot be directly compared for
    equality.]{tags=":communicate:"}
6.  [Use "short-circuit" logical expressions in a
    program.]{tags=":program:"}
7.  [Evaluate the result/side-effects of "short-circuit" logical
    expressions.]{tags=":evaluate:"}
8.  [Use nested `else if` blocks in a program.]{tags=":program:"}
9.  [Evaluate a code snippet containing complex conditional statements
    and logical expressions.]{tags=":evaluate:"}

Loops
-----

By the end of this unit, students should be able to:

1.  [Write code that repeats execution with loop control
    structures.]{tags=":program:"}
    1.  Use a `for` loop to repeat an operation on a fixed number of
        items (exactly $n$ times).
    2.  Use a `while` loop to repeat an operation while some condition
        is `true` (0 or more times).
    3.  Use a `do`/`while` loop to repeat an operation while some
        condition is `true` (1 or more times).
    4.  Choose the appropriate looping structure for a specific
        situation.
2.  [Convert code that uses a `for` loop to a `while` loop, and
    vice-versa.]{tags=":program:"}
3.  [Evaluate the execution of a loop control
    structure.]{tags=":evaluate:"}
    1.  List the order of operations for both `for` and `while` loop
        control structures in Java/Processing.
4.  [Discover the cause of crashing software by inspecting a stack
    trace.]{tags=":program:"}

Advanced Loops
--------------

By the end of this unit, students should be able to:

1.  [Write code that uses a nested looping structure to solve a
    problem.]{tags=":program:"}
    1.  Identify when a nested loop should be used to solve a problem.
2.  [Evaluate the execution of a nested looping
    structure.]{tags=":evaluate:"}
    1.  List the order of operations of a nested looping structure.
    2.  List the state of variables in a nested looping structure.
3.  [Write code that uses arbitrarily nested control structures (i.e.,
    conditional statements, loops) to solve a
    problem.]{tags=":program:"}
4.  [Manage the state of execution by using using a boolean variable to
    indicate that an event has happened.]{tags=":program:"}

User Defined Functions Part 2
-----------------------------

By the end of this unit, students should be able to:

1.  [Apply top-down programming to simplify and solve complex
    problems.]{tags=":algorithms:"}
    1.  Break a problem down into smaller, functional units.
    2.  Decide how much logic belongs in a single function.
    3.  Decide what inputs and outputs a function requires based on what
        it will do.
2.  [Use stub functions to help write code for a previously broken-down
    problem.]{tags=":program:"}
3.  [Create and use user-defined functions that accept one or more
    parameters and/or `return` data to the caller in a
    program.]{tags=":program:"}
    1.  Choose when to use globally-scoped variables and when to use
        locally-scoped variables/function parameters.
    2.  Pass data to a function by reference, and pass data to a
        function by value.
    3.  Use sentinel values to communicate an exceptional situation or
        error.
4.  [Create and use an [accumulator] variable in a
    program.]{tags=":program:"}
    1.  Iteratively build a `String` by appending characters to the
        empty string.
    2.  Take a running sum of a value by adding numbers to zero.
    3.  Choose an appropriate initial value for an accumulator variable.
5.  [List the state and scope of variables by tracing the execution of
    code when user-defined functions are called.]{tags=":evaluate:"}
    1.  Distinguish between multiple variables with the same name in
        different scopes.
6.  [Define the term "side-effects", in relation to calling functions,
    passing values by reference, and global
    variables.]{tags=":communicate:"}

  [accumulator]: https://en.wikipedia.org/wiki/Accumulator_(computing)

Compiling and the Java Virtual Machine
--------------------------------------

By the end of this unit, students should be able to:

1.  [Describe the workflow that a computer takes, going from high-level
    code, to a computer program running on your
    computer.]{tags=":communicate:"}
    1.  Define the terms "compiler", "high-level language", "machine
        language", "virtual machine", "source code".
    2.  Explain the purpose of a compiler.
    3.  Explain the purpose of a virtual machine.

Array Basics
------------

By the end of this unit, students should be able to:

1.  [Identify kinds of values that require "collection
    types".]{tags=":represent:"}
2.  [Create and use arrays in a program.]{tags=":program:"}
    1.  Get the length of an array.
    2.  Iterate over an array with a loop.
    3.  Initialize an array with literals.
3.  [List the limitations of an array.]{tags=":communicate:"}
4.  [Compare and contrast `String`s and arrays.]{tags=":communicate:"}

Arrays and Memory
-----------------

By the end of this unit, students should be able to:

1.  [Name the default value stored in an array, immediately after
    creation, based on type.]{tags=":communicate:"}
2.  [Use and compare variables against `null`.]{tags=":program:"}
3.  [Copy the contents of one array to another.]{tags=":program:"}
4.  [Compare the contents of two arrays.]{tags=":program:"}
5.  [Compare and contrast arrays and primitive
    types.]{tags=":communicate:"}
    1.  Explain why the assignment operator does not copy the contents
        of an array.
    2.  Explain why the equality relational operator does not compare
        the contents of two arrays.

Arrays and Functions
--------------------

By the end of this unit, students should be able to:

1.  [Use arrays as arguments and return values to and from
    functions.]{tags=":program:"}
    1.  Modify data in an array passed as an argument.
2.  [Explain why arrays as arguments behave differently from primitive
    variables.]{tags=":communicate:"}

Working with Arrays: Techniques
-------------------------------

By the end of this unit, students should be able to:

1.  [Apply strategies for working with partially-filled
    arrays.]{tags=":program:"}
    1.  [Use a "pointer" value (an index) to represent the next free
        location.]{tags=":algorithms:"}
    2.  [Choose and use an appropriate "sentinel" value to represent
        unused locations in the array (e.g., `null`, negative numbers,
        numbers outside the range of values being
        represented).]{tags=":represent:"}
2.  [Explain the limitations of partially-filled
    arrays.]{tags=":communicate:"}
    1.  List strategies for overcoming the limitations of partially
        filled arrays.
3.  [Describe the linear search algorithm in plain
    English.]{tags=":algorithms:"}
    1.  [Give an example of data where linear search might be
        used.]{tags=":communicate:"}
    2.  [Explain the limitations of linear
        search.]{tags=":communicate:"}
4.  [Implement the linear search algorithm on an
    array.]{tags=":program:"}
5.  [Describe the binary search algorithm in plain
    English.]{tags=":algorithms:"}
    1.  [Give an example of data where binary search might be
        used.]{tags=":communicate:"}
    2.  [Explain the limitations of binary
        search.]{tags=":communicate:"}
6.  [Implement the binary search algorithm on an
    array.]{tags=":program:"}
7.  [Measure the complexity of linear search and binary
    search.]{tags=":algorithms:"}
8.  [Compare and contrast linear search and binary
    search.]{tags=":algorithms:"}
    1.  [State the requirements on data for binary search to be
        applied.]{tags=":communicate:"}
9.  [Use "parallel" arrays to represent compound information for a
    single entity (i.e., `name[0]` and `age[0]` represent the same
    person).]{tags=":represent:"}
    1.  [Write a program that uses parallel arrays.]{tags=":program:"}
