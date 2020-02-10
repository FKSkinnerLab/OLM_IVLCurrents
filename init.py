# from mpi4py import MPI
from neuron import h

h.load_file("SynParamSearch.hoc")
# execfile("RunSims.py")
exec(open("RunSims.py").read())
h.quit()
sys.exit(0)