# 1D-Heat-Equation

## Overview

The 1D heat equation is

$$
\frac{\partial u}{\partial t} = k\frac{\partial u^2}{\partial x^2}
$$

where u is the temperature, t is time, x is space, and k is the thermal diffusivity constant. The initial condition for the heat equation is

$$
u(x, 0) = f(x) 
$$

for 0 < x < L, where f(x) is a function and L is the spatial domain.

## Boundary Conditions

This model uses Dirichlet boundary conditions; that is, the temperature at x = 0 and x = L is fixed to be zero. Mathematically, this is

$$
u(0, t) = u(L, t) = 0
$$

for t > 0.

## The Fourier Problem

Combining the above equations gives an initial-boundary value problem, or a Fourier problem:

$$
\frac{\partial u}{\partial t} = k\frac{\partial u^2}{\partial x^2}; \quad 0 < x < L, \quad t > 0
$$

$$
u(x, 0) = f(x); \quad 0 < x < L
$$

$$
u(0, t) = u(L, t) = 0; \quad t > 0
$$

The above Fourier problem can be solved via Fourier Analysis for an analytical solution or by a numerical method.

## The Analytical Solution

To obtain the analytical solution, apply the method of separation of variables and then, assuming that f(x) is piecewise smooth, Fourier Series can be used. Doing so gives,

$$
u(x, t) = \sum_{n = 1}^{\infty} a_{n}e^{\frac{-kn^2\pi^2t}{L^2}}\sin({\frac{n\pi x}{L}})
$$

where $a_n$ is a Fourier coefficient given by

$$
a_n = \frac{2}{L}\int_{0}^{L} f(x)\sin({\frac{n\pi x}{L}})dx
$$

For full details on the analytical solution, see the file "Analytical_Solution.md".

## Numerical Methods

The Fourier problem above can also be solved numerically. The numerical method used in this model is the forward time-centered space method (FTCS). In this method, a forward finite difference approximation is applied to the time derivative, that is

$$
\frac{\partial u}{\partial t} \approx \frac{u_i^{(j+1)} - u_i^{(j)}}{\Delta t}
$$
