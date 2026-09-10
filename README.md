# 1D-Heat-Equation

## Overview

The 1D heat equation is a parabolic partial differential equation (PDE), which is mathematically represented as

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

For the spatial derivative, a centered difference approximation is applied:

$$
\frac{\partial u^2}{\partial x^2} \approx \frac{u_{i-1}^{(j)} - 2u_i^{(j)} + u_{i+1}^{(j)}}{\Delta x^2}
$$

Then, the update formula becomes:

$$
u_i^{(j+1)} = ru_{i+1}^{(j)} + (1 - 2r)u_i^{(j)} + ru_{i-1}^{(j)}
$$

For full details on the numerical solution, see the file "Numerical_Solution.md".

## Running the Model



## Model Input

The following parameters are needed to run this model (with the default value in parentheses):

k -> This is the thermal diffusivity constant (DEFAULT = 1)

L -> This is the domain space (DEFAULT = 1)

r -> Represents stability (defined above; DEFAULT = 4)

nx -> This is the number of spatial intervals (DEFAULT = 40)

dx = L / nx -> This is the grid spacing

dt = r * dx**2 / k -> This is the time grid

T_fin -> This is the final time (end time; DEFAULT = 0.5)

N = round(T_fin / dt)

Initial condition (DEFAULT: np.sin((np.pi)*x))

Boundary conditions -> Dirichlet (i.e., both boundaries are 0)

## Output Example

The output shown below was generated using the default values (listed above)



## Future Ideas

1. Explore the effects of different initial conditions. For example, f(x) = $x^2$, f(x) = tan(x), f(x) = $\frac{1}{x}$, etc.
2. Explore the effects of non-zero boundary conditions (i.e., non-Dirichlet BCs). Try incorporating Neumann boundary conditions within the model.
3. Examine how the rate of temperature decay is impacted by variations in the thermal diffusivity constant, k.
4. Employ an alternative temporal update, such as a Crank-Nicolson scheme. Doing so should yield a tridiagonal system, which can be solved using a Successive Over-Relaxation (SOR) method. Compare the convergence rates between the two numerical methods.

## Packages

The packages needed to run this model are:

1. numpy
2. matplotlib
3. mplot3d from mpl_toolkits

## Reference Links

