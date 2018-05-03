transDatabase = [ ['a', 'c','e'], ['b','c','e'],
		['a','b','c','e'], ['b','e'] ]
# This holds the itemsets that frequenty occur in the database
# A list of sets

frequencyList = [ ]

# A candidate list - the cardinality of Fk with each element in the database
# A list of sets

candidateList = [ ]

# 1 initialize the frequencyList
# Find the longest set in the database

maxSetLength = 0
for currentSet in transDatabase :
	if (len(currentSet) > maxSetLength) :
		maxSetLength = len(currentSet)

# Creating [ set1, set2, ... set-maxSetLength] where all sets are emtpy

for index in range(maxSetLength) :
	frequencyList.append(set())

print(frequencyList)

# generate C(1)-- candidateList1 and F(1) frequencyList

candidateMap = { }
for currentSet in transDatabase :
	for element in currentSet :
		print(element)
	
		if candidateMap.get[element] != 0 :
			candidateMap[element] + 1;
			candidateMap[element] + 1
		else :
			candidateMap[element] = 1

print(candidateMap)




	
