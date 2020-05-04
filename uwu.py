import sys,time,random

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
while True:
    slow_type("Starting The UwU-nizer.  .  .  .\n\n")
    slow_type(" _   ___      ___   _")
    slow_type("\n| | | \ \ /\ / / | | |")
    slow_type("\n| |_| |\ V  V /| |_| |\n")
    slow_type(" \__,_| \_/\_/  \__,_|")
    slow_type("\n\n\nDone! UwU-Nization complete")
