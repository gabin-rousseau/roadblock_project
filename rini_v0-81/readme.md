### May 2024, author: Gabin ROUSSEAU, supervisors: Edward Wallace and Ramon Grima
### This folder contains the final version of the rini project.

Files include:

__rini_v0-81.ipynb__ - Main jupyter notebook, contains the code for the model itself (rini - initial version, TASEP with targeted dynamic defects, a.k.a. "independence model"; corini - alternative version, roadblock dynamics feature a cooperativity component, a.k.a. "cooperativity" model).

__rini_v0-81_keyfigures.ipynb__ - Jupyter notebook containing the code used to generate the key figures from the Honours project dissertation. (Phase diagram, experiment to model boxplot comparisons and parameter space exploration.)
__rinipy.py__ - Python3 file that packages together the dependencies needed to run the (co)rini_paramscore functions from the keyfigures notebook.
Because rini_parascore uses parallel processing, it is recommended to load in rinipy with the following:
from rinipy import rini_INIvBLOCK as rib
from rinipy import corini_INIvBLOCK as cib

__rini_v0-81_extras.ipynb__ - Jupyter notebook containing miscellaneous code used to explore the model's outputs (e.g., average occupany of every site as time=t...)
