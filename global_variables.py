#!/usr/bin/env python 3

# Created by: Wajd Mariam
# Created on: Sept 2019
# This program shows how local and global variables works

# global variable
variable_X = 25


def local_variable():
    # This variable shows what's happening with local_variable

    variable_X = 10
    variable_Y = 30
    variable_A = variable_X + variable_Y
    print("local variable_X, variable_Y, variable_A: {0} + {1} = {2}"
          .format(variable_X, variable_Y, variable_A))


def global_variable():
    # This variable shows what's happening with global_variable

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_A = variable_X + variable_Y
    print("Global variable_X, variable_Y, variable_A : {0} + {1} = {2}"
          .format(variable_X, variable_Y, variable_A))


def main():
    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
