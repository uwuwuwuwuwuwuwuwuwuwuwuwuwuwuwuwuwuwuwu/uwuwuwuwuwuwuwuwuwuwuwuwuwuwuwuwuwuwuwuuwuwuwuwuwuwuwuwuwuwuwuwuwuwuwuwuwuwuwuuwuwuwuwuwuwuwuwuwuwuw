import sys,time,random

slow_typing_speed = 50 #wpm
fast_typing_speed = 100 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/slow_typing_speed)
def fast_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/fast_typing_speed)

slow_type("Starting the UwU-nizer.  .  .  .\n\n")
while True:
    slow_type(" _   ___      ___   _")
    slow_type("\n| | | \ \ /\ / / | | |")
    slow_type("\n| |_| |\ V  V /| |_| |\n")
    slow_type(" \__,_| \_/\_/  \__,_|")
    slow_type("\n\n\nDone! UwU-Nization Complete.\n")
    fast_type("Restarting the UwU-nizer.  .  .  .\n")
    time.sleep(3)
    fast_type("Successfully Restarted the UwU-nizer.\n\n")
