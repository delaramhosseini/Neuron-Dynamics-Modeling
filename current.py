from pymonntorch import Behavior
import torch


class ConstanceCurrent(Behavior):
    def initialize(self, ng):
        self.current = self.parameter("current", None)
        self.noise_range = self.parameter("noise_range", 0)
        
        ng.I = ng.vector(self.current)
        
        
    def forward(self, ng):
        rand = (ng.vector("uniform") - 0.5) * self.noise_range
        ng.I = ng.vector(self.current) + rand
    


class SinCurrent(Behavior):
    def initialize(self, ng):
        self.wave_length = self.parameter("wave_length", 1)
        self.current_range = self.parameter("current_range", 1)
        self.noise_range = self.parameter("noise_range", 0)
        
        ng.I = ng.vector(0)
        
    def forward(self, ng):
        sin = ((torch.sin(ng.vector(ng.network.dt * ng.network.iteration) / self.wave_length) ) +1 ) * self.current_range / 2
        rand = (ng.vector("uniform") - 0.5) * self.noise_range
        
        ng.I = rand + sin
        
        
class StepCurrent(Behavior):
    def initialize(self, ng):
        self.t0 = self.parameter("t0", 0)
        self.ش = self.parameter("current", 10)
        self.noise_range = self.parameter("noise_range", 0)
        
        ng.I = ng.vector(0)
        
    def forward(self, ng):
        rand = (ng.vector("uniform") - 0.5) * self.noise_range
        if self.t0 < ng.network.iteration * ng.network.dt:
            ng.I = ng.vector(self.current) + rand
        ng.I += rand
        

class UniformCurrent(Behavior):
    def initialize(self, ng):
        self.current = self.parameter("current", 10) * 2
        self.tau = self.parameter("tau_I",1)
        self.noise_range = self.parameter("noise_range", 0)
        
        ng.I = ng.vector("uniform") * self.current
        
    
    def forward(self, ng):
        rand = (ng.vector("uniform") - 0.5) * self.noise_range
        ng.I += (ng.vector("uniform") - (ng.I/self.current)) * self.tau + rand
        



        
        