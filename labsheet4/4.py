from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

local_data = (rank, rank ** 2)
all_data = comm.gather(local_data, root=0)

if rank == 0:
    print("Collected Data:", all_data)