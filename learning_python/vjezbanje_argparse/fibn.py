import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
        
def Main():
    parser = argparse.ArgumentParser()
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quite", action="store_true")
    
    parser.add_argument("num", help="The Fibonacci number you wish to calculate", type=int)
    parser.add_argument("-o", "--output", help="Output the result to a file", action="store_true")
    
    args = parser.parse_args()
    
    res = fib(args.num)
    
    if args.verbose:
        print "The "+str(args.num)+"th fib numer is "+str(res)
    elif args.quite:
        print res
    else:
        print "Fib("+str(args.num)+") = " + str(res)
    
    if args.output:
        f = open("finonacci.txt", "a")
        f.write(str(res)+"\n")
    
if __name__ == "__main__":
    Main()