This model uses a Forward Time-Centered Space (FTCS) Method to solve the 1D Heat Equation numerically. This is an explicit method, as each value can be updated independently. The FTCS Method is also conditionally stable, meaning that if the stability parameter exceeds a certain threshold, the model blows up. 

Recall the 1D Heat Equation:

$$
\frac{\partial u}{\partial t} = k\frac{\partial u^2}{\partial x^2}
$$

where u is the temperature, t is time, x is space, and k is the thermal diffusivity constant. We apply a forward finite difference approximation to the time derivative:

$$
\frac{\partial u}{\partial t} \approx \frac{u_i^{(j+1)} - u_i^{(j)}}{\Delta t}
$$

For the spatial derivative, a centered difference approximation is applied:

$$
\frac{\partial u^2}{\partial x^2} \approx \frac{u_{i-1}^{(j)} - 2u_i^{(j)} + u_{i+1}^{(j)}}{\Delta x^2}
$$

Note that we omit the truncation errors (for completeness, the time truncation error is first order, while the spatial truncation error is second order). We then apply the above two approximations to the 1D Heat Equation:

$$
\frac{u_i^{(j+1)} - u_i^{(j)}}{\Delta t} = k \frac{u_{i-1}^{(j)} - 2u_i^{(j)} + u_{i+1}^{(j)}}{\Delta x^2}
$$

Since FTCS is an explicit method, as mentioned before, we solve for $u_i^{(j+1)}$:

$$
u_i^{(j+1)} = 
$$
