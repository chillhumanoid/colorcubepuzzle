# Color Cube Puzzle Solver

## The Puzzle
You have 4 cubes, and the idea is that when you have them together, you have 4 squares on each "side". The puzzle is to get it so that each cube has only 1 of each color. 

Cube 1 has the following adjacent pairs
* green-red
* red-white
* blue-white

Cube 2 has the following adjacent pairs
* red-green
* green-green
* blue-white

Cube 3 has the following adjacent pairs
* red-white
* white-green
* green-blue

Cube 4 has the following adjacent pairs
* red-red
* blue-green
* white-blue

## The Solution
* create the 4 cubes
* get all possible ways each cube can be placed. 
* put those 4 cube lists into one big list, with every possible combination of those 4 cubes (list(produce(c1...) on line 18)
* check each combination and remove any combination from the master list that won't work (have two of the same color on any given side). Runs through this 4 times.
* go through the final solutions to eliminate ones that are actually the same (given that we really don't care where the colors are, just what's on the 4 public facing sides and which side)
* print the final solution. 
