'''
README

output list is nearly ready to be
copy/pasted into code,
but you need to remember to 
add a " before the first
and afer the last index of the list,
and indent the rows properly
because it outputs a string, not a list.

outputList is of type String
inputList is of type list/array

Input:
["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10"])
Expected output: 
Test1", "Test2", "Test3", "Test4", "Test5"
 "Test6", "Test7", "Test8", "Test9", "Test10
'''


inputList = ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10"]

#adjust the n value to change how many
#columns there are in outputList
n = 5

lines = []
line = []

for i, word in enumerate(inputList, start=1):
    line.append(word) 
    if i % n == 0:
        lines.append('", "'.join(line))
        line = []
if line:
    lines.append('", "'.join(line))
outputList = '"\n "'.join(lines)


print(outputList)