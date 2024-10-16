import matplotlib.pyplot as plt


def print_plot(net, title = ""):
    plt.plot(net["ng1_rec",0].variables["u"])
    plt.ylabel("votage")
    plt.xlabel("time")
    plt.show()
    
    plt.plot(net["ng1_rec",0].variables["I"])
    plt.ylabel("current")
    plt.xlabel("time")
    plt.show()
    
    plt.plot(net["ng1_rec",0].variables["w"])
    plt.ylabel("adaptive_variable")
    plt.xlabel("time")
    plt.show()
    
    
    plt.scatter(net["ng1_even",0].variables["spike"][:, 0].cpu(), net["spike", 0][:, 1].cpu())
    plt.ylabel("spike")
    plt.xlabel("time")
    plt.show()
    


    
    
    
    
    
        
