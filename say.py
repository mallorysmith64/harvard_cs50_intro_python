import cowsay
import sys

#run python3 say.py <your_first_name>
if(len(sys.argv) == 2):
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])
    