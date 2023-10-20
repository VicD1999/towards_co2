from gboml import GbomlGraph
import gboml.compiler.classes as gcc

import json
import os
import sys
from datetime import datetime
import argparse

# from utils import *

# if needed use click to be able to change the arguments of the main and the configuration.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', help='Name gboml file',
                        type=str, default="algeria")
    parser.add_argument('-y', '--years', help='Number of years',
                        type=int, default=3)
    parser.add_argument('-c', '--cap_co2', help="Cap on CO2 if None no cap on CO2",
                        type=float, default=0.0)
    parser.add_argument('-cost_co2', '--co2_emission_cost', help="Cost on CO2 in M€/kt",
                        type=float, default=80*10**(-3))
    parser.add_argument('-ens', '--e_ens_cost', help="Cost on ens in M€/GWh",
                        type=float, default=3.)
    parser.add_argument('-sc', '--scenario', help="Number of scenrio",
                        type=int, default=0)
    parser.add_argument('-p_c', "--pipe_carrier", help="Select constraint",
                        choices=["pipe_and_boat", "only_carrier", "only_pipe"],
                        default="pipe_and_boat")
    args = parser.parse_args()

    name = args.name
    years = args.years
    cap_co2 = args.cap_co2
    co2_emission_cost = args.co2_emission_cost
    e_ens_cost = args.e_ens_cost
    scenario = args.scenario
    constraint = args.pipe_carrier
    ens_permitted = False
    
    timehorizon = 24*365*years

    gboml_model = GbomlGraph(timehorizon=timehorizon)
    nodes, edges, param = gboml_model.import_all_nodes_and_edges(args.name + ".gboml")

    # Scenario with cap on CO2, No ens and Carrier
    co2_emission_cost = 0
    constraint="only_carrier"

    def modify_param_node(ls_nodes, name_node, name_param, value_param):
        for n in ls_nodes:
            if n.name == name_node:
                print(n.name)
                # l = list(map(lambda x: x.replace(p,param_to_add),l))
                param_to_add = gcc.Parameter(name_param, gcc.Expression("literal", value_param))   
                for p in n.parameters:
                    if p.get_name() == name_param:
                        p = param_to_add
                        print(p)
                        
                        # n.parameters.replace(p, param_to_add)
                        # n.parameters.remove(p)
                # param_to_add = gcc.Parameter(name_param, gcc.Expression("literal", value_param))    
                # n.parameters = list(map(lambda x: x.replace(p_to_modify,param_to_add), n.parameters))
                        
                        # n.parameters.append(param_to_add)
    import pandas as pd
    df = pd.read_csv("data/samples.csv")

    idx = 7

    capex_pcc = df.iloc[idx]["capex_pcc"]
    capex_co2_liq_plant = df.iloc[idx]["capex_co2_liq_plant"]
    capex_co2_regas = df.iloc[idx]["capex_co2_regas"]
    capex_co2_carrier = df.iloc[idx]["capex_co2_carrier"]
    capex_dac = df.iloc[idx]["capex_dac"]
    capex_co2_liq_storage = df.iloc[idx]["capex_co2_liq_storage"]

    # MODIFY CAPEX
    modify_param_node(ls_nodes=nodes, name_node="PCCC", name_param="capex", value_param=capex_pcc)
    modify_param_node(ls_nodes=nodes, name_node="PCCC_CCGT", name_param="capex", value_param=capex_pcc)

    modify_param_node(ls_nodes=nodes, name_node="CO2_LIQUEFACTION_PLANTS", name_param="full_capex", value_param=capex_co2_liq_plant)
    modify_param_node(ls_nodes=nodes, name_node="LIQUEFIED_CO2_REGASIFICATION", name_param="full_capex", value_param=capex_co2_regas)

    modify_param_node(ls_nodes=nodes, name_node="LIQUEFIED_CO2_CARRIERS", name_param="full_capex", value_param=capex_co2_carrier)
    modify_param_node(ls_nodes=nodes, name_node="DIRECT_AIR_CAPTURE_PLANTS", name_param="full_capex", value_param=capex_dac)

    modify_param_node(ls_nodes=nodes, name_node="LIQUEFIED_CO2_STORAGE_BE", name_param="full_capex_stock", value_param=capex_co2_liq_storage)
    modify_param_node(ls_nodes=nodes, name_node="LIQUEFIED_CO2_STORAGE", name_param="full_capex_stock", value_param=capex_co2_liq_storage)


    # Boat or pipe This line is needed otherwise too many constraints
    # edges, nodes = pipe_and_or_boat(nodes=nodes, edges=edges, constraint=constraint)

    gboml_model.add_global_parameters(param)
    gboml_model.add_nodes_in_model(*nodes)
    gboml_model.add_hyperedges_in_model(*edges)
    gboml_model.build_model()
    solution, obj, status, solver_info, constr_info, _ = gboml_model.solve_gurobi("options.opt", details="details.txt")
    print("Solved")
    gathered_data = gboml_model.turn_solution_to_dictionary(solver_info, status, solution, obj, constr_info)
    print("Json done")
  
    if not os.path.exists("UQ"):
        os.makedirs("UQ")
        
    with open(f'UQ/f"{idx}_T_{timehorizon}_{capex_pcc}_{capex_co2_liq_plant}_{capex_co2_regas}_{capex_co2_carrier}_{capex_dac}_{capex_co2_liq_storage}"sc_{args.scenario}_T_{timehorizon}.json', "w") as fp:
        json.dump(gathered_data, fp, indent=4)
