import sys,time,random

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
slow_type("Starting The UwU-nizer.  .  .  .\n\n")
while True:
    slow_type(" _   ___      ___   _")
    slow_type("\n| | | \ \ /\ / / | | |")
    slow_type("\n| |_| |\ V  V /| |_| |\n")
    slow_type(" \__,_| \_/\_/  \__,_|")
    slow_type("\n\n\nDone! UwU-Nization complete")
    slow_type("Restarting the UwU-nizer.  .  .  .\n")
    time.sleep(2)
    slow_type("The UwU-nizer is almost ready.  .  .  .\nPlease wait.  .  .  .")
    time.sleep(2)
