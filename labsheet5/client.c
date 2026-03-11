#include "add.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    CLIENT *cl;
    addin in;
    addout *out;

    if (argc != 4) {
        printf("Usage: client <machine> <int1> <int2>\n");
        return 1;
    }

    /* Create RPC client */
    cl = clnt_create(argv[1], ADD_PROG, ADD_VERS, "tcp");
    if (cl == NULL) {
        clnt_pcreateerror(argv[1]);
        exit(1);
    }

    /* Set input values */
    in.arg1 = atol(argv[2]);
    in.arg2 = atol(argv[3]);

    /* Call remote procedure */
    out = add_proc_1(&in, cl);

    if (out == NULL) {
        clnt_perror(cl, "RPC call failed");
    } else {
        printf("We received the result: %ld\n", *out);
    }

    /* Destroy client */
    clnt_destroy(cl);

    return 0;
}
