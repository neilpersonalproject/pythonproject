# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import simpy as sy
import random


random.seed(1)
num_servers = 24
num_scanners = 15
runTime = 600
total_time = 0
total_passengers = 1
num_passengers = 500

class Airport(object):
    """ID/boarding pass check queue and security scanning
    """
    def __init__(self, env, num_servers, num_scanners):
        self.env = env
        self.server = sy.Resource(env, num_servers)
        self.scanner = sy.Resource(env, num_scanners) 
        
        
    def IDcheck(self, passenger):
        """The ID check process. It takes a "person", checks their ID,then 
        passes him/her to the next step."""
        ID_service_time = random.expovariate(.75)
        yield self.env.timeout(ID_service_time)

    def scan(self, passenger):
        """Security Scan. Passenergs are sent to shortest queue then scanned"""
        scan_time = random.uniform(0.5, 1)
        yield self.env.timeout(scan_time)
        
def Passenger(env, number, s):
    """Passnegers arrive, to the first available server for the ID check then
    sent to the first available scanner.
    """
    global total_time #global average wait time
    global total_passengers    
    Arrivaltime = env.now
    with s.server.request() as request:
        yield request
        yield env.process(s.IDcheck(number))


    with s.scanner.request() as request:
        yield request
        yield env.process(s.scan(number))
    
    pass_time = env.now - Arrivaltime
    total_time = total_time + pass_time
    total_passengers = total_passengers+1

def setup(env, num, security):
    arrival_int = random.expovariate(5)
    yield env.timeout(arrival_int)
    env.process(Passenger(env, num, security))

# Setup and start the simulation
print('Airport Security')
random.seed(1)
env = sy.Environment()
ap = Airport(env, num_servers, num_scanners)
# Start processes and run
for i in range(0,num_passengers):
    env.process(setup(env, i, ap))

env.run()

avg_time = total_time / total_passengers
print("avg_time")
print(avg_time)