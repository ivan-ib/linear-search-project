linear search project

this project is a python program that shows exactly how a linear search algorithm works. The interface is made using gradio.



what the program does:

linear search starts at the beginning of the list and looks at each number in order. if it finds the target, it stops and returns the index. if it reaches the end without finding it, the target is not in the list.



how linear search works (algorithm steps):

1. reads the list of numbers
2. starts at index 0
3. compares the current value to the target
4. if they match, return the index
5. if not, move to the next index
6. if the end of the list is reached, the target is not found



computational thinking:

decomposition

- take the user's list
- go through each number
- compare each number to the target
- return the steps and the result

pattern recognition

- the same action is repeated for every item: check → compare → move forward
- works the same way for lists of any size

abstraction

- the user does not see how the loop works
- the interface only shows the list, the target, and the steps

algorithm design

input: list of numbers and a target  
process: convert inputs to integers, then use linear search  
output: list of steps and result (found or not found)


how to run the program

locally
1. install python
2. install gradio:
