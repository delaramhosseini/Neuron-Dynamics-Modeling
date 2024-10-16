from pymonntorch import Behavior
import torch


class lif(Behavior):
    def initialize(self, ng):
        self.tau = self.parameter("tau", None, required=True)
        self.u_rest = self.parameter("u_rest", None, required=True)
        self.u_reset = self.parameter("u_reset", None, required=True)
        self.R = self.parameter("R", None, required=True)
        self.threshold = self.parameter("threshold", None, required=True)
        self.ratio = self.parameter("ratio", None, required=True)
        
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
        ng.u += ((-(ng.u - self.u_rest) 
                  + (self.R * (ng.I 
                               * (ng.network.iteration - ng.last_spike  > self.T).byte()))) 
                 * ng.network.dt) / self.tau
        ng.spike = ng.u > self.threshold
        ng.u[ng.spike] = self.u_reset
        
        ng.last_spike[ng.spike] = ng.network.iteration
        

        
        

