# f=open("sample.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this:

with open("sample.txt") as f:
    print(f.read())