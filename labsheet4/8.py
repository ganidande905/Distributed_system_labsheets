from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    comm.send("Confidential Message", dest=2)
elif rank == 2:
    data = comm.recv(source=0)
    print(f"Process {rank} received: {data}")