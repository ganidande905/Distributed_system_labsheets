from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 2:
    print("Run the program with at least 2 processes.")
    exit()

if rank == 0:
    print("Process 0: Sending 'ping' to Process 1")
    comm.send("ping", dest=1)
    message = comm.recv(source=1)
    print(f"Process 0: Received message from Process 1: {message}")

elif rank == 1:
    message = comm.recv(source=0)
    print(f"Process 1: Received message from Process 0: {message}")
    comm.send("pong", dest=0)
    print("Process 1: Sent 'pong' to Process 0")