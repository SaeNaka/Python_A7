# 世界人口ランキングn位

import sys
args = sys.argv
rank = int(args[1])

population_tuple = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
print(population_tuple[rank-1], end="")