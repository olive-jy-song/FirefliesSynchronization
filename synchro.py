# the following code was performed in Jupyter Notebook 
# the (actual-MEAN) phases were ploted rather than the actual phases 
# vertical shifts in the plots do not influence observations 

import numpy as np
import matplotlib.pyplot as plt 

N = 100
Kr = 0.4
pi = np.pi 
w = 50
dt = 0.01

step_size = 200
flies_index = [i for i in range(N)]
flies_ini_phase = np.random.uniform(-pi,pi,N) 
curr_phase = flies_ini_phase 
phases_minus_mean = []  

def calculate_phases(phase_arr, step_size, dt): 
    for t in range (0,step_size):    
        phase_mean = np.mean(phase_arr)  
        for i in range (0,N): 
            phase_arr[i] += w + dt * Kr * np.sin(phase_mean-phase_arr[i])
    phases_minus_mean = phase_arr - np.mean(phase_arr) 
    return phases_minus_mean 

def plot_phases(phase_arr): 
    plt.scatter(flies_index, phase_arr) 
    plt.xlabel('Index of Fireflies')
    plt.ylabel('Phases') 
    
plot_phases(curr_phase)
plt.title('Randomly Initialized Fireflies Phases')
print("The average phase is ", np.mean(curr_phase)) 
print("The standard deviation of phase is ", np.std(curr_phase)) 

# the following lines were used repeatedly for 200, 400, 600, ... steps 
phases_minus_mean = calculate_phases(curr_phase, step_size, dt) 
plot_phases(phases_minus_mean) 
plt.title('Fireflies Phases After # Steps')
