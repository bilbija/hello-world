import time
import sys


def progress(count, total, fill=">", empty="."):
    bar_len = 50
    filled = int(round(bar_len*count/float(total)))
    percents = round(count/float(total)*100)
    bar = filled*fill+(bar_len-filled)*empty
    
    sys.stdout.write("[%s] %d%s\r" %(bar, percents,"%"))
    sys.stdout.flush()
#- end progress


if __name__ == "__main__":
    speed = 0.05
    print "Download progress:"
    for i in range(101):
        progress(i, 100)
        time.sleep(speed)
    print ""
    print "This is The END :( !"
##-- end __main__