# Sudoku-Image-Solver

## The goal
A program that reads an input file with a sudoku and returns a solved one.

## Description
This project was inspired by an article on TowardsDataScience. However, this is my own approach. I'm using or-tools as a 'constraint programming device' - 
very quick solution with little amount of code. Simple CpModel and CpSolver are enough, the solver itself contains just the 3 obligatory constraints:
- different numbers in rows
- different numbers in columns
- different numbers in cells.

In order to read images, MNIST dataset is used to train.

From that, an algorithm with proper readings of hough lines is be applied (with cv2). 
Finally, previously mentioned solver will take care of the rest.

## Files
The code can be divided into 5 sections:
1. Training Reader - reads the MNIST Dataset.
2. Solver - OR-Tools sovler.
3. Model - model (compiling and fitting), confusion matrix and metrics.
4. Image Reader - reads image and lines.
5. Digit Prediction - reads digits from each cell and builds a sudoku.

The program is compiled in that order. 

## Example usage
Current version of the code contains image _example.png_ (![found here](https://www.theguardian.com/lifeandstyle/2019/nov/18/sudoku-4612-easy)).
After building the model we can see it's summary in jupyter and the confusion matrix. As can be seen, it has a nice, slightly over 99% accuracy.
![Conf](/results/confusion_matrix.png?raw=true "Confusion matrix")

From there we go into image reading and digit predicting. 
The image with drawn lines should be displayed, and logs written in console.

![Logs](/results/logs.jpg?raw=true "First logs after predicting an image")

In order to make sure that sudoku is feasible and properly read, probabilities are being saved in DigitPrediction class. 
A question about sudoku is asked to a user. If the data displayed is correct, 'yes' should be written.

![Resultsfalse](/results/result1.jpg?raw=true "Incorrect sudoku")

If the sudoku is not correct - a simple 'no' answer would get us into handler. For each digit with probability smaller than 70% a question is asked.

![Results](/results/result2.jpg?raw=true "Corrected version")

Finally, a result for a sudoku is displayed.

![Answer](/results/answer.jpg?raw=true "Solved sudoku")



