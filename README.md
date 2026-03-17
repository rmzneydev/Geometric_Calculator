# Geometric Calculator (CLI)

A simple **Command Line Interface (CLI) Geometric calculator written in
Python**. This program allows users to select geometric figures and
calculate properties such as:

-   Perimeter
-   Angles
-   Area
-   Volume
-   Circumference

The calculator supports both **2D and 3D geometric figures** and uses an
interactive menu system.

------------------------------------------------------------------------

# Features

## 2D Figures

-   Triangle
-   Right Triangle
-   Rectangle
-   Hexagon
-   Circle

## 3D Figures

-   Cube
-   Sphere
-   Cylinder
-   Rectangular Prism

## Available Calculations

Depending on the figure selected, the program can calculate:

-   **Perimeter**
-   **Angles**
-   **Area**
-   **Volume**
-   **Circumference**

The program automatically shows only the calculations that are valid for
the selected figure.

------------------------------------------------------------------------

# Project Structure
```bash
geometry-calculator/
│
├── start_menu.py
├── calculations.py
└── README.md
```
Project documentation

------------------------------------------------------------------------

# How to Run

## 1. Clone the repository

git clone https://github.com/yourusername/Geometric-calculator.git

## 2. Navigate to the project folder

cd Geometric-calculator

## 3. Run the program

python start_menu.py

------------------------------------------------------------------------

# Input Validation

The program includes validation to ensure:

-   Only valid numbers are accepted
-   Values must be greater than zero
-   Angles follow geometric rules (e.g., triangle angle sum \< 180°)

------------------------------------------------------------------------

# Example Calculations

## Triangle Area

Area = (base × height) / 2

## Circle Area

Area = π × r²

## Cylinder Volume

Volume = π × r² × height

------------------------------------------------------------------------

# Requirements

-   Python 3.x
-   No external libraries required

------------------------------------------------------------------------

# Possible Improvements

Future improvements could include:

-   Adding more geometric figures
-   Adding graphical visualization
-   Exporting results
-   Converting the CLI into a GUI application
-   Adding unit tests

------------------------------------------------------------------------

# Author

Developed by **Neyder Ramirez**.
