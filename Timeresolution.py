from pymonntorch import Behavior
import torch

class timeresolution(Behavior):
    def initialize(self, network): 
        network.dt = self.parameter("dt", 1)
        
    def forward(self, object):
        pass
    