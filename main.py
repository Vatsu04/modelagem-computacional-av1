import simpy
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import call as Call
import env as env



# Criação do ambiente de simulação

env = simpy.Environment()
env.now = 0
env.process(env.now)
