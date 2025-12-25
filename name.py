import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")
    
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    
for arg in sys.argv[1:]: #[1:-1] would get rid of first and last
    print("Hello, my name is", arg)