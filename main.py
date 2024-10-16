import pymonntorch as pmt
from LIF import lif
from Timeresolution import timeresolution
from project1.current import constancecurrent
from ELIF import Elif
import torch

import matplotlib.pyplot as plt

    
net = pmt.Network(behavior = {1: timeresolution(dt = 1)} )


ng1 = pmt.NeuronGroup(size = 3,
                  net = net,
                  behavior = {
                      2 : constancecurrent(current = 8),
                      3 : lif(tau=10,
                              R=1.7,
                              u_rest=-67,
                              u_reset=-75,
                              threshold=-55,
                              ratio=1),
                      4 : pmt.Recorder(variables=["u","I"], tag="ng1_rec"),
                      5 : pmt.EventRecorder(tag="ng1_event", variables=["spike"])
                  })


ng2 = pmt.NeuronGroup(size = 1,
                  net = net,
                  behavior = {
                      2 : constancecurrent(current = 10),
                      3 : Elif(tau=10,
                              R=1.7,
                              delta=1,
                              u_rest=-67,
                              u_reset=-75,
                              threshold=-13,
                              u_rh=-50,
                              ratio=1),
                      4 : pmt.Recorder(tag="ng2_rec", variables=["u"]),
                      5 : pmt.EventRecorder(tag="ng2_event", variables=["spike"])
                  })


net.initialize()
net.simulate_iterations(100)


plt.plot(net["ng1_rec",0].variables["u"])
plt.show()


