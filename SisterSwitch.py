print("-----------------------------------------------------------------\n")
#Dictionary of Sisters and their phone numbers
sisters = {}

#Array of sisters names, will be used as key to get phone number values
sistersA = []
print(len(sistersA))

#Dictionary of new members names and phone numbers
newMembers = {}

#Array of new members names, will be used as the key to get the phone number value
newMembersA = [ ]

print(len(newMembersA))

mustGroup = {}

mustGroupA = []

print(len(mustGroupA))

import random
#Random suffle 3 arrays
random.shuffle(sistersA)
random.shuffle(newMembersA)
random.shuffle(mustGroupA)

indexS = 0
indexN = 0
indexM = 0
group = 1

while(group != 12):
    print("\n\nGroup " + str(group))
    print("------------------------")
    group = group + 1
    print(sistersA[indexS] + "\t" + sisters[sistersA[indexS]])
    print(sistersA[indexS + 1] + "\t" + sisters[sistersA[indexS + 1]])
    print(sistersA[indexS + 2] + "\t" + sisters[sistersA[indexS + 2]])
    print(sistersA[indexS + 3] + "\t" + sisters[sistersA[indexS + 3]])
    print(newMembersA[indexN] + "\t" + newMembers[newMembersA[indexN]])
    print(newMembersA[indexN + 1] + "\t " +newMembers[newMembersA[indexN + 1]])
    print(mustGroupA[indexM] + "\t" + mustGroup[mustGroupA[indexM]])
    print(mustGroupA[indexM + 1] + "\t" + mustGroup[mustGroupA[indexM + 1]])
    indexS = indexS + 4
    indexN = indexN + 2
    indexM = indexM + 2

print("\n\n\nMembers left over: \n---------------------------\n" + mustGroupA[indexM]+ " " + mustGroup[mustGroupA[indexM]])

print(mustGroupA[indexM + 1] + "\t" + mustGroup[mustGroupA[indexM + 1]])
print(mustGroupA[indexM + 2] + "\t" + mustGroup[mustGroupA[indexM + 2]])
print(mustGroupA[indexM + 3] + "\t" + mustGroup[mustGroupA[indexM + 3]])
