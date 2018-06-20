import time
 
# Save current timestamp to a variable named start. (Unix timestamp) using the module time and the method of that module called time aswell.
start = time.time()
 
# Sleep for two second using time module sleep function
time.sleep(2)
 
# Save ending timestamp to a variable named end.
end = time.time()
 
#Print time difference between end and start.
print(int(end-start))



#Now, lets use the time module to take the runtime of our program:

import time

# Save start timestamp to a variable named start. (Unix timestamp)
def take_time(sleep_time):
    start = time.time()
    
    # Do something!
    o = 1
    for i in range(10)
        o *= i
        time.sleep(0.2)
    
    # Save ending timestamp to a variable named end.
    end = time.time()

    #Print time difference between end and start, rounded to integer to skip all the decimals.
    print("It took", int(end-start, 2), "seconds to run our loop")
