# Runge-Kutta Methods (RK2 and RK4)
This repository contains Python implementations of two popular numerical integration methods: the second-order Runge-Kutta method (RK2) and the fourth-order Runge-Kutta method (RK4). These methods are widely used in scientific and engineering applications for solving ordinary differential equations (ODEs) numerically.

## Table of Contents
Introduction
Usage
Examples
Contributing
License
Introduction
Runge-Kutta methods are numerical techniques used to approximate the solutions of initial value problems (IVPs) for ordinary differential equations. They are based on Taylor series expansions and provide accurate results by evaluating the derivative at multiple points within a time step.

# RK2 (Second-Order Runge-Kutta Method)
The RK2 method, also known as the midpoint method, calculates the derivative at two points within each time step to approximate the solution. It is a second-order accurate method, meaning that the local truncation error is on the order of O(h^3), where h is the time step size.

# RK4 (Fourth-Order Runge-Kutta Method)
The RK4 method is an extension of the RK2 method and is one of the most widely used numerical integration methods. It evaluates the derivative at four points within each time step, providing a higher accuracy compared to RK2. RK4 is a fourth-order accurate method, with a local truncation error of O(h^5).
