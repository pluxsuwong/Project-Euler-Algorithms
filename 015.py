# Problem 15 - Lattice Paths
print "Problem 15 - Lattice Paths"

c = 1
for i in range(21, 41):
    c *= i
r = 1
for i in range(1, 21):
    r *= i
print c / r
