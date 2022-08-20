def scope():
    def do_local():
        t= "local test"
    def do_non_local():
        nonlocal t
        t = "non local test"
    def do_globel():
        global t
        t = "globel test"
    t= "defualt"
    do_local()
    print("test value after do_local :"+t)
    do_non_local()
    print("test value after do_non_local :"+t)
    do_globel()
    print("test value after d0_globel :"+t)
scope()
print("test value after d0_globel :"+t)
