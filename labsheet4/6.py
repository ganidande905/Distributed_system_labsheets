from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    role = "Manager"
elif rank == 1:
    role = "Worker A"
elif rank == 2:
    role = "Worker B"
elif rank == 3:
    role = "Worker C"

print(f"Process {rank} role: {role}")