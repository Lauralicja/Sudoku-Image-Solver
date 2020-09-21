# I am a simple solver.
# Written using Or-Tools.
from __future__ import print_function
import numpy as np
from ortools.sat.python import cp_model

class Solver:
    def __init__(self):
        self.model = cp_model.CpModel()
        self.solver = cp_model.CpSolver()
        self.grid_size = 9
        self.cell_size = 3

    def get_values(self, solution, original_grid):
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                if original_grid[row, column] == 0:
                   solution[row, column] = self.model.NewIntVar(1, 9, '(%i,%i)' % (row, column))
                else:
                   solution[row, column] = self.model.NewConstant(int(original_grid[row, column]))
        return solution

    def printer(self, solution):
        for i in range(self.grid_size):
            if i % 3 == 0:
                print("\n")
            for j in range(self.grid_size):
                if j % 3 == 0 and j != 0:
                    print(" ", end = " ")
                print(self.solver.Value(solution[i,j]), end=" ")
            print()

    def solve(self, grid):
        solutions = {}

        # Get ints from grid
        solutions = self.get_values(solutions, grid)

        ##---CONSTRAINTS---
        # Horizontals
        for row in range(self.grid_size):
            line_horizontal = []
            for column in range(self.grid_size):
                line_horizontal.append(solutions[row, column])
            self.model.AddAllDifferent(line_horizontal)

        # Verticals
        for column in range(self.grid_size):
            line_vertical = []
            for row in range(self.grid_size):
                line_vertical.append(solutions[row, column])
            self.model.AddAllDifferent(line_vertical)

        # Squares
        for row_idx in range(0, self.grid_size, self.cell_size):
            for col_idx in range(0, self.grid_size, self.cell_size):
                self.model.AddAllDifferent([solutions[row_idx + row, column] for column in range(col_idx, (col_idx + self.cell_size)) 
                                            for row in range(self.cell_size)])

        # Solve model
        status = self.solver.Solve(self.model)
        self.printer(solutions)
