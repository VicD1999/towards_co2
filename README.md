# Towards CO2 Valorization in a multi remote renewable energy hub framework with uncertainty quantification

Repository for our scientific paper results: https://orbi.uliege.be/handle/2268/309679 .


# Installation

First you need to setup your environment:

```pip install -r requirements. txt```

You can use any management of environment you want the installed libraries are standard:
matplotlib, numpy, pandas. 

The only special library is gboml. You can find the documentation and installation guide here:
https://gboml.readthedocs.io/en/latest/


# How to use the code

In order to reproduce the results obtained in the article run:

```python3 main.py -sc $num_scenario -y 2```

There are 5 scenarios from 1 to 5. 

Therefore, ```$num_scenario \in {1, 2, 3, 4, 5}```

# Uncertainty Quantification (UQ)

The file uq.py is responsible for solving the system for a given sample.

```python uq.py -sc 1 -y 2 -idx $sample```

The UQ analysis is performed using https://github.com/rheia-framework/RHEIA .

This analysis was performed independently of this repository. 

All results are discussed in https://orbi.uliege.be/handle/2268/309679 . 



# Cite
Please, if you use this code in your work consider citing https://orbi.uliege.be/handle/2268/309679 : 

@unpublished{ORBi-43e7b54f-5adb-4f0f-b7e0-d203cd5b2aed,
	AUTHOR = {Dachet, Victor and Benzerga, Amina and Coppitters, Diederik and Contino, Francesco and Fonteneau, Raphaël and Ernst, Damien},
	TITLE = {Towards CO2 valorization in a multi remote renewable energy hub framework with uncertainty quantification},
	LANGUAGE = {English},
	YEAR = {2023},
	ABSTRACT = {In this paper, we propose a multi-RREH (Remote Renewable Energy Hub) based optimization framework. This framework allows a valorization of CO2 using carbon capture technologies. This valorization is grounded on the idea that CO2 gathered from the atmosphere or post combustion can be combined with hydrogen to produce synthetic methane. The hydrogen is obtained from water electrolysis using renewable energy (RE). Such renewable energy is generated in RREHs, which are locations where RE is cheap and abundant (e.g., solar PV in the Sahara Desert, or wind in Greenland). We instantiate our framework on a case study focusing on Belgium and 2 RREHs, and we conduct a techno-economic analysis under uncertainty. This analysis highlights, among others, the interest in capturing CO2 via Post Combustion Carbon Capture (PCCC) rather than only through Direct Air Capture (DAC) for methane synthesis in RREH. By doing so, a notable reduction of 10% is observed in the total cost of the system under our reference scenario. In addition, we use our framework to derive a carbon price threshold above which carbon capture technologies may start playing a pivotal role in the decarbonation process of our industries. For example, this price threshold may give relevant information for calibrating the EU Emission Trading System so as to trigger the emergence of the multi-RREH.}
}



