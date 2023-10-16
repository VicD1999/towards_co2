import gboml.compiler.classes as gcc

def pipe_and_or_boat(nodes, edges, constraint="pipe_and_boat"):
    """
    Remove PIPE_CO2, PIPE_CO2_GR or CARRIER_CO2, CARRIER_CO2_GR from the edges and nodes.
    
    Select constraints in:
    PIPE_CO2_CONNECTION
    COASTAL_CARBON_DIOXIDE_BALANCE
    COASTAL_CARBON_DIOXIDE_BALANCE_GR
    
    Parameters
    ----------
    edges : list
        List of edges
    nodes : list
        List of nodes
    constraint : str
        Str to choose between ["pipe_and_boat", "only_carrier", "only_pipe"]
    
    Returns
    -------
    edges : list
        New list of edges
    nodes : list
        New list of nodes
    """
    ls_edges = ["PIPE_CO2_CONNECTION", "COASTAL_CARBON_DIOXIDE_BALANCE", 
                "COASTAL_CARBON_DIOXIDE_BALANCE_GR", "POWER_LINE", 
                "COASTAL_LIQUEFIED_METHANE_BALANCE_GR", "COASTAL_LIQUEFIED_METHANE_BALANCE"]
    
    constraints = ["pipe_and_boat", "only_carrier", "only_pipe"]

    assert constraint in constraints
    constraints.remove(constraint)

    if constraint == "pipe_and_boat":
        ls_nodes = []
    elif constraint == "only_carrier":
        ls_nodes = ["PIPE_CO2", "PIPE_CO2_GR"]
    elif constraint == "only_pipe":
        ls_nodes = ["CARRIER_CO2", "CARRIER_CO2_GR"]

    for e in edges:
        
        if e.name in ls_edges:
            # print(e.name)
            e.constraints = list(filter(lambda x: x.name not in constraints, e.constraints))


    nodes = list(filter(lambda x: x.name not in ls_nodes, nodes))
    
    return edges, nodes

def remove_cap(edges):
    """
    Remove cap CO2 from edges
    
    Parameters
    ----------
    edges : list
        List of edges
        
    Returns
    -------
    edges : list
        New edges
    """
    edges = list(filter(lambda x: x.name != "CAP_CO2", edges))
    return edges

def cap(param, cap_co2):
    """
    Update cap_co2 parameter
    
    Parameters
    ----------
    param : list
        List of parameters
    cap_co2 : float
        value of cap_co2
        
    Returns
    -------
    param : list
        New list of parameters
    """
    param = list(filter(lambda x: x.name != "cap_co2", param))
    param.append(gcc.Parameter("cap_co2", 
                            gcc.Expression("literal", cap_co2)))

    return param

def emission_cost(param, co2_emission_cost):
    """
    Update co2_emission_cost parameter
    
    Parameters
    ----------
    param : list
        List of parameters
    co2_emission_cost : float
        value of co2_emission_cost
        
    Returns
    -------
    param : list
        New list of parameters
    """
    param = list(filter(lambda x: x.name != "co2_emission_cost", param))
    param.append(gcc.Parameter("co2_emission_cost", 
                            gcc.Expression("literal", co2_emission_cost)))

    return param

def set_ens_cost(param, e_ens_cost):
    """
    Update e_ens_cost parameter
    
    Parameters
    ----------
    param : list
        List of parameters
    e_ens_cost : float
        value of e_ens_cost
        
    Returns
    -------
    param : list
        New list of parameters
    """
    param = list(filter(lambda x: x.name != "e_ens_cost" , param))
    param.append(gcc.Parameter("e_ens_cost", 
                            gcc.Expression("literal", e_ens_cost)))

    return param

def ens_allowed(nodes):
    """
    Remove ens==0 from ENERGY_DEMAND_BE nodes constraints
    
    Parameters
    ----------
    nodes : list
        List of nodes
        
    Returns
    -------
    nodes : list
        New list of nodes
    """
    for n in nodes:
        if n.name == "ENERGY_DEMAND_BE":
            for c in n.constraints:
                if c.get_name() == "dual_constraint":
                    n.constraints.remove(c)

    return nodes