import ipdb
from lib.animal import *
from lib.zoo import *


# code here

# e.g.
#   z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
#   a1 = Animal( 'Lion', 75, 'Luke', z1 )

z1 = Zoo("Riverbanks Zoo", "Columbia, SC")
Animal("Tiger", 75, "Luke", z1)
Animal("Tiger", 42, "Leia", z1)
Animal("Snake", 25, "Jake", z1)

z3 = Zoo("Riverbanks Gardens", "Columbia, SC")
Animal("Elephant", 38, "Eddy", z3)


z2 = Zoo("Micke Grove Zoo", "Lodi, CA")
Animal("Tiger", 100, "Tony", z2)
Animal("Tiger", 123, "John", z2)


# do not remove
ipdb.set_trace()
