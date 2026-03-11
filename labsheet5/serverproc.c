struct addin {
    long arg1;
    long arg2;
};

typedef long addout;

program ADD_PROG {
    version ADD_VERS {
        addout ADD_PROC(addin) = 1;
    } = 1;
} = 0x3543000;
root@e3f315ec8ecb:~/labsheet# cat serverproc.c
#include "add.h"

addout *add_proc_1_svc(addin *in, struct svc_req *rqstp)
{
    static addout result;

    result = in->arg1 + in->arg2;

    return &result;
}
