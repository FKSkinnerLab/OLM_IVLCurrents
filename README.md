# OLMng
"Next-generation" multi-compartment model of CA1 hippocampal O-LM interneurons
==============================================================================

Run this script to plot the current traces across somatic and dendritic compartments in the OLMng models (see https://github.com/FKSkinnerLab/OLMng). Note that this code was written for use with python 2.7 and will require some minimal alterations for use in python 3. Edit "init_model.py" to change from model 1 (i.e. Gormadoc) to model 2 (i.e. Isembard). In the plotting codes the "Cell_Name" variable also needs to be changed to either 'Gormadoc' or 'Isembard'.

Model invocation
----------------
Before running the simulations you must first compile the mod files using the following command:

    nrnivmodl

To run simulations use python as a command-line argument as follows:

    python init.py

After running the simulations npy files will save the current traces to the NPY_files folder and the following additional options will be available.

To plot current traces:

    python PlotCurrentPairs.py

To plot current X current cross-correlations:

    python PlotCurrentXCorrs.py

To plot current X voltage cross-correlations:

    python PlotVoltageXCorrs.py

To plot cross-correlations across compartments (currents):

    python PlotMorphXCorrs.py

To plot cross-correlations across compartments (voltage):

    python PlotMorphXCorrsV.py

List of cells
-------------
The cells currently available are:

ID      Name
------------

1       Gormadoc

2       Isembard


Model parameters
----------------
Most parameters are found in either the sim_params.hoc file or in the 
per-cell parameter files within the "param_files" directory. The ones in
sim_params.hoc are particularly relevant for global aspects of operation
such as length of simulation, integration method, current clamp injection
parameters, etc. 
# OLM_IVLCurrents
