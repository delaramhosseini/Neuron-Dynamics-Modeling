from pymonntorch import Behavior
import torch

class Elif(Behavior):
    def initialize(self, ng):
        self.tau = self.parameter("tau", None)
        self.u_rest = self.parameter("u_rest", None)
        self.u_reset = self.parameter("u_reset", None)
        self.R = self.parameter("R", None)
        self.u_rh = self.parameter("u_rh", None)
        self.threshold = self.parameter("threshold", None)
        self.delta = self.parameter("delta", None)
        self.ratio = self.parameter("ratio", None)
        
        #Resistance range
        self.T = self.parameter("T", 0) / ng.network.dt
        
        #voltage
        ng.u = ng.vector("uniform")  * (self.threshold - self.u_reset) * self.ratio
        ng.u += self.u_reset
        
        #spike
        ng.spike = ng.u > self.threshold
        ng.u[ng.spike] = self.u_reset
        ng.last_spike = ng.vector(-self.T-1)
        
        
        #adaptability
        ng.w = ng.vector(0)
        
    
    def forward(self, ng):
        lekage = -(ng.u - self.u_rest)
        input_u = self.R * (ng.I 
                               * (ng.network.iteration - ng.last_spike  > self.T).byte()) 
        exp_part = self.delta * torch.exp((ng.u - self.u_rh) / (self.delta or 1))
        ng.u += ng.network.dt * (lekage + exp_part + input_u) / self.tau

        ng.spike = ng.u > self.threshold
        
        ng.u[ng.spike] = self.u_reset
        
    