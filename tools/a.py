def get_ip(number='10', start='1.1.1.1'):
    starts = start.split('.')
    A = int(starts[0])
    B = int(starts[1])
    C = int(starts[2])
    D = int(starts[3])
    for A in range(A, 256):
        for B in range(B, 256):
            for C in range(C, 256):
                for D in range(D, 256):
                    ip = "%d.%d.%d.%d" % (A, B, C, D)
                    return ip
                    

arr = []
for i in range(10):
    a = get_ip(10, '172.1.13.70')
    arr.append(a)
print(arr)