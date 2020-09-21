# Sudoku-Image-Solver

## The goal
To create a program that will read an input file with a sudoku and return a solved one.

## Description
This project was inspired by an article on TowardsDataScience. However, this is my own approach. I'm using or-tools as a 'constraint programming device' - 
very quick solution with little amount of code. Simple CpModel and CpSolver are enough, the solver itself contains just the 3 obligatory constraints:
- different numbers in rows
- different numbers in columns
- different numbers in cells.

In order to read images, MNIST dataset is used to train.

From that, an algorithm with proper readings of hough lines will be applied (with cv2). 
Finally, previously mentioned solver will take care of the rest.

## Current version
It is still a work in progress. Current version contains a proper solver, dataset handler and a very simple network (most likely to change).

Solver class is working and can be used as a separate program for calculating sudoku.




