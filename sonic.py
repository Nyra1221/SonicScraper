import google, random, sys, webbrowser, os, hedge

print "Mental Disorder Simulator 2016. Type !rs in the y/n field to restart. If you've had enough, type !exit to close." + "\n"

mode = raw_input("You can input names manually, or have the program select a random one for you. (manual/random) ")
if mode.lower() == "manual":
    hedge.search()
if mode.lower() == "!exit":
    sys.exit()
else:
    hedge.rand()
end = raw_input("You've escaped.. Press enter to restart. You know you want to! ")

os.execl(sys.executable, sys.executable, *sys.argv)
 

