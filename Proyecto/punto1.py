# PUNTO 1

class DisjSet:

    def __init__(self, n):
        # Constructor to create and initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    # Finds set of given item x

    def find(self, x):

        # Finds the representative of the set that x is an element of
        if (self.parent[x] != x):

            # if x is not the parent of itself
            # Then x is not the representative of
            # its set,
            self.parent[x] = self.find(self.parent[x])

            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set
            # (self.parent[x])
        return self.parent[x]

    # Do union of two sets represented
    # by x and y.

    def Union(self, x, y):

        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

    def LeerInstrucciones(self, string):

        string = string.split(" ")

        query = str(string[0].rstrip())
        a = int(string[1].rstrip())
        b = int(string[2].rstrip())

        if query == "3":
            print(obj.find(a) == obj.find(b))
        elif query == "2":
            i = a
            while i <= b:
                obj.Union(a, i)
                i = i+1
        elif query == "1":
            obj.Union(a, b)


f = open("P1test9.in", "r")
primera = f.readline()
primera = primera.split(" ")

num_departamentos = int(primera[0])+1
num_queries = primera[1]

obj = DisjSet(num_departamentos)

for x in f:
    obj.LeerInstrucciones(str(x).replace("\t", " "))

f.close()


"""
obj.Union(2, 5)
obj.Union(4, 2)
obj.Union(3, 1)

# Ver si estan en el mismo set
if obj.find(2) == obj.find(5):
    ('Yes')
else:
    ('No')

if obj.find(1) == obj.find(0):
    ('Yes')
else:
    ('No')"""
