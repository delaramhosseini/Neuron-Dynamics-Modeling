# Neuron Dynamics Modeling
This project focuses on simulating and analyzing various neuron models, including LIF, ELIF, and AELIF, to understand their dynamics and the effects of different input currents and parameters.

## Project Objectives
1. Understand the processes involved in simulating and implementing computational models of neurons.
2. Analyze dynamic neuron models and their behaviors.

## Activities
1. Implement LIF (Leaky Integrate-and-Fire), ELIF (Exponential Leaky Integrate-and-Fire), and AELIF (Adaptive Exponential Leaky Integrate-and-Fire) models using the Euler method. 
   - Utilize different input currents such as pulse functions, sinusoidal waves, etc. 
   - Investigate the performance of each neuron model at varying input current intensities.
   - Plot the changes in membrane potential over time for different conditions.
   
2. For cases where the input neuron generates a desired current along with noise, plot the changes in membrane potential under various noise levels.

3. For neuron models using a steady current, plot the Frequency-Current (F-I) relationship.
   - Subsequently, add noise to the input current and analyze the results.

4. Simple implementation of the refractory period into these models.
   - Explore different methods for incorporating the refractory process to prevent input currents from affecting the model immediately after an action potential.

5. Perform experiments across a range of parameters to analyze the behavior of different neuron models.
   - Document the results and draw conclusions on the effects of various parameters on neuron dynamics.

## Requirements
- Python and relevant libraries for simulation (e.g., NumPy, Matplotlib).

## Usage
1. Clone the repository:
   ```bash
   git clone <repository-url>
