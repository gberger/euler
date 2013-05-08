N = range(10,99)
D = range(10,100)

for n in N:
    for d in D:
        if n<d:
            ns = str(n)
            ds = str(d)
            try:
                if ns[0] == ds[0] and float(ns[1])/float(ds[1]) == float(n)/d:
                    print n, d
                if ns[1] == ds[1] and float(ns[0])/float(ds[0]) == float(n)/d:
                    print n, d
                if ns[0] == ds[1] and float(ns[1])/float(ds[0]) == float(n)/d:
                    print n, d
                if ns[1] == ds[0] and float(ns[0])/float(ds[1]) == float(n)/d:
                    print n, d
            except ZeroDivisionError:
                pass