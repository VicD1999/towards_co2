from gboml import GbomlGraph
import json
import os
import sys
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# from analysis import MakeMeReadable 


if __name__ == '__main__':

    filename = "analysis.json"

    results = {}
    with open(filename, "r") as fp:
        results = json.load(fp)
        
    num_scenarios = len(results)

    names, var = results["1"]["new_power_capacity"].keys(), results["1"]["new_power_capacity"].values()

    print(f"scenario & ", end='')
    for name in names:
        print(f"{name} & ", end='')
    print("\\\\ \\hline")

    for sc in range(1,num_scenarios+1):
        print(f"{sc} & ", end='')
        _, var = results[str(sc)]["new_power_capacity"].keys(), list(results[str(sc)]["new_power_capacity"].values())
        for i in range(len(var)):
            v = var[i]
            if i < len(var) - 1: 
                print(f"{v:.2f} & ", end='')
            else:
                print(f"{v:.2f} \\\\", end='')
            
        print()

    names, var = results["1"]["total_power_capacity"].keys(), results["1"]["total_power_capacity"].values()

    print(f"scenario & ", end='')
    for name in names:
        print(f"{name} & ", end='')
    print("\\\\ \\hline")

    for sc in range(1,num_scenarios+1):
        print(f"{sc} & ", end='')
        _, var = results[str(sc)]["total_power_capacity"].keys(), list(results[str(sc)]["total_power_capacity"].values())
        for i in range(len(var)):
            v = var[i]
            if i < len(var) - 1: 
                print(f"{v:.2f} & ", end='')
            else:
                print(f"{v:.2f} \\\\ ", end='')
            
        print("")

    names, var = results["1"]["co2_capture"].keys(), results["1"]["co2_capture"].values()

    print(f"scenario & ", end='')
    for name in names:
        print(f"{name} & ", end='')
    print("\\\\ \\hline")

    for sc in range(1,num_scenarios+1):
        print(f"{sc} & ", end='')
        _, var = results[str(sc)]["co2_capture"].keys(), list(results[str(sc)]["co2_capture"].values())
        for i in range(len(var)):
            v = var[i]
            if i < len(var) - 1: 
                print(f"{v:.2f} & ", end='')
            else:
                print(f"{v:.2f} \\\\ ", end='')
            
        print("")

    keys = ['pipe_nz', 'carrier_nz', 'pipe_gr', 'carrier_gr']

    print(f"Scenario & ", end="")
    for i in range(len(keys)):
        print(f"{keys[i]} & ", end="")
    print("\\\\")
    print("\\hline")
    for sc in range(1,num_scenarios+1):
        print(f"{sc} & ", end='')
        for i in range(len(keys)):
            if i < len(keys) - 1: 
                try:
                    print(f"{results[str(sc)][keys[i]]:.3f} & ", end="")
                except:
                    print(f" - & ", end="")
            else:
                try:
                    print(f"{results[str(sc)][keys[i]]:.3f} ", end="")
                except:
                    print(f" - ", end="")
        print("\\\\")

    print(f"Scenario & ", end="")
    for i in range(1, num_scenarios+1):
        print(f"{i} & ", end="")
    print("\\\\")
    print(f"€/MWh & ", end="")
    for sc in range(1, num_scenarios+1):
        cost = results[str(sc)]["ch4_cost_per_kwh"] * 1000 
        print(f"{cost:.2f} & ", end="")

    print("\\\\")


