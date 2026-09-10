This model uses a Forward Time-Centered Space (FTCS) Method to solve the 1D Heat Equation numerically. This is an explicit method, as each value can be updated independently. The FTCS Method is also conditionally stable, meaning that if the stability parameter exceeds a certain threshold, the model blows up. 

Recall the 1D Heat Equation:

$$
\frac{\partial u}{\partial t} = k\frac{\partial u^2}{\partial x^2}
$$

where u is the temperature, t is time, x is space, and k is the thermal diffusivity constant.

