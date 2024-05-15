import sys
args = sys.argv
#引数を変数に代入
rank = int(args[1])

#タプルを作成
population = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

population_rank = population[rank - 1]
print(population_rank, end = '')