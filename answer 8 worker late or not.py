# I check to see if the worker is on time
time = int(input('What time did the worker get to work? '))
late_time = int(input('What time is the worker late? '))

if time is 8  and late_time > 8:
    on_time = True 
else: late_time = False

# somewhere later in your code if you need to check if worker is
# on time, all I need to do is check the boolean variable
# I set earlier in my code
if on_time:
    print('the worker is on time')