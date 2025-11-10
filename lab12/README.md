# Lab 12: Fractal Trees

A Python program that generates fractal tree images using recursion and the PIL library.

## What it does
The `tree.py` program generates beautiful fractal tree images. The process involves:
- Creating a Tree object with initial position and branching parameters
- Growing the tree recursively for a specified number of generations (age)
- Each branch splits into multiple smaller branches at different angles
- Branches get progressively smaller with each generation (fractal pattern)
- Color gradient from trunk (brown) to small branches (lighter brown/tan)
- Rendering the final tree to an image file using PIL (Python Imaging Library)

The program demonstrates:
- Recursive generation of fractal patterns
- Using external graphics libraries (PIL/Pillow) for image creation
- Working with geometric transformations (rotation, scaling)
- Color gradients and RGB color values
- Converting mathematical concepts (angles in radians) to visual output
