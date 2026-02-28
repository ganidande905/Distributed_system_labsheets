from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    comm.send("Data for Process 1", dest=1)
    comm.send("Data for Process 2", dest=2)
    comm.send("Data for Process 3", dest=3)
else:
    data = comm.recv(source=0)
    print(f"Process {rank} received: {data}")