def check_scope():
    def do_local():
        test = "local test"

    def do_non_local():
        nonlocal test
        test = "Non local test"

    def do_global():
        global  test
        test = "Global test"

    test = "Default"
    do_local()
    print("Test Value after do_local() is : "+test)
    do_non_local()
    print("Test Value after do_non_local() is : " + test)
    do_global()
    print("Test Value after do_global() is : " + test)

check_scope()
print("test value after main is : "+test)
