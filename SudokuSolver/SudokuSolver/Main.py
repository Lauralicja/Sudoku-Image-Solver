from TrainingReader import TrainingReader
from Solver import Solver
from Model import Model
import numpy as np
from keras import Sequential

if __name__ == "__main__":

    print("\n---------------")
    trainer = TrainingReader()
    trainer.read_mnist()

    print(trainer.input_shape)
    print("\n---------------")

    model_class = Model()
    model_class.create_model()





    grid =  np.array([[0,0,0, 2,6,0, 7,0,1],
                    [6,8,0, 0,7,0, 0,9,0],
                    [1,9,0, 0,0,4, 5,0,0],

                    [8,2,0, 1,0,0, 0,4,0],
                    [0,0,4, 6,0,2, 9,0,0],
                    [0,5,0, 0,0,3, 0,2,8],

                    [0,0,9, 3,0,0, 0,7,4],
                    [0,4,0, 0,5,0, 0,3,6],
                    [7,0,3, 0,1,8, 0,0,0]])


    print("\n---------------")
    sudoku_solver = Solver()
    print("Solving the sudoku...")
    sudoku_solver.solve(grid)
    print("\nHope you're happy with that solution!")
    print("\n---------------")
