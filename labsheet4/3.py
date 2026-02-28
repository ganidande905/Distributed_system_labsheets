from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [(10, 'A'), (20, 'B'), (30, 'C'), (40, 'D')]
else:
    data = None

received = comm.scatter(data, root=0)
print(f"Process {rank} received: {received}")