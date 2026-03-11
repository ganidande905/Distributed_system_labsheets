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
