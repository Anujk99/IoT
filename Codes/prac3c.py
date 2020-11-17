############### Practical : ######################
# Print current time for 10 times with an interval of 10 seconds.
#----------------------------------------------------------------

import time

def current_time():
    for i in range(10):
        ct = time.ctime()
        print(f"current time is: {ct}")
        time.sleep(10)



if __name__=="__main__":
    current_time()
