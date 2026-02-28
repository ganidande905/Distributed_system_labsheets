from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [1, 2, 3, 4]
else:
    data = None

received = comm.scatter(data, root=0)
processed = received * received
result = comm.gather(processed, root=0)

if rank == 0:
    print("Squared Results:", result)