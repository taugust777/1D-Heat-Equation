#Tim August
#3 / 16 / 26

#1D Heat Equation
#FTCS

#The 1D heat equation is:
    #u_t = k*u_xx for 0 < x < L and t > 0
        #L is the domain; t is the time

#The initial condition is:
    #u(x, 0) = f(x) for 0 < x < L

#The boundary conditions for this model are taken to be Dirichlet:
    #u(0, t) = u(L, t) = 0 for t > 0

#This model will compare a numerical solution with the analytical solution

#The analytical solution is obtained via a Fourier analysis:
    #u(x, t) = sigma (n = 1 -> inf) a_n*exp(-k*n^2*pi^2*t / L^2)*sin(n*pi*x / L)

#The numerical solution is obtained by implementing a forward time-centered space numerical scheme
    #A forward finite difference approximation is applied to u_t
    #A central finite difference method is applied to u_xx
    #The update formula is then:
        #u_i^(j+1) = r*u_i+1^(j) + (1-2r)*u_i^(j) + r*u_i-1^(j)
        #Here, r = k*delta t / delta x^2

#_________________________________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Parameters
k = 1 #This is the thermal diffusivity constant
L = 1 #This is the domain space
r = 0.4 #Represents stability (defined above)

nx = 40 #This is the number of spatial intervals
dx = L / nx #This is the grid spacing

dt = r * dx**2 / k #This is the time grid
T_fin = 0.5 #This is the final time (end time)
N = round(T_fin / dt)

#Arrays for solutions
    #Choose all zeros and then can advance

numerical_solution = np.zeros((nx + 1, N + 1))
analytical_solution = np.zeros((nx + 1, N + 1))

#Grids for x space and t space
x = np.linspace(0, L, nx + 1)
t = np.linspace(0, T_fin, N + 1)

#_________________________________________________________________________________________________________________________
#Initial conditions and boundary conditions

#Initial condition: let f(x) = sin(pi*x)
numerical_solution[:, 0] = np.sin((np.pi)*x)

#Boundary condition: Dirichlet (i.e., both boundaries are 0)
numerical_solution[0, :] = 0
numerical_solution[-1, :] = 0

#__________________________________________________________________________________________________________________________
#Now, find the analytical solution
#Sub in formula from above (see documentation for details on the Fourier solution):

for j in range(N + 1):
    analytical_solution[:, j] = np.exp((-k * (np.pi)**2 * t[j]) / L**2) * np.sin(((np.pi) * x) / L)

#__________________________________________________________________________________________________________________________
#Now find the numerical solution
#Use the advance formula listed above (see documentation for details):

for j in range(N):
    for i in range(1, nx):
        numerical_solution[i, j + 1] = r * numerical_solution[i + 1, j] + \
                                       (1 - 2*r)*numerical_solution[i, j] + \
                                       r * numerical_solution[i - 1, j]

#_________________________________________________________________________________________________________________________
#Compute the error between the analytical and numerical solutions (pick max error) and then plot

error = np.abs(numerical_solution - analytical_solution)
max_error = np.max(error[:, -1])
print("Max error between analytical and exact solutions: ", max_error)

#Plot
#Do a two-panel plot
    #1. Numerical vs. analytical solutions
    #2. Surface plot of the numerical solution

T, X = np.meshgrid(t, x)


fig = plt.figure(layout = "compressed")

#1.
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, analytical_solution[:, -1], color = "black", label = "Analytical Solution")
ax1.plot(x, numerical_solution[:, -1], color = "darkorange", label = "Numerical Solution", linestyle = ":")

ax1.set_xlabel("Space", fontsize = 8)
ax1.set_ylabel("Temperature", fontsize = 8)
ax1.tick_params(axis = "x", labelsize = 7)
ax1.tick_params(axis = "y", labelsize = 7)

ax1.set_title("Numerical vs. Analytical Solutions", fontsize = 9)
ax1.legend(fontsize = 8)


#2.
ax2 = fig.add_subplot(1, 2, 2, projection = "3d")
surf = ax2.plot_surface(T, X, numerical_solution, cmap = "afmhot")

ax2.set_xlabel("Time", fontsize = 8)
ax2.set_ylabel("Space", fontsize = 8)
#ax2.set_zlabel("Temperature")
ax2.tick_params(axis = "x", labelsize = 7)
ax2.tick_params(axis = "y", labelsize = 7)
ax2.tick_params(axis = "z", labelsize = 7)

ax2.set_title("Surface Plot for Numerical Solution", fontsize = 9)

cbar = fig.colorbar(surf, ax = ax2, shrink = 0.6, pad = 0.12)
cbar.set_label("Temperature", fontsize = 8)
cbar.ax.tick_params(labelsize = 7)

plt.show()
