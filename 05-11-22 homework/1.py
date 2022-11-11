# Write a program to print the following number patterns using a loop.
# a)
# 	1
# 	1 	2
# 	1	2	3
# 	1	2	3	4
# 	1	2	3	4	5

n=5
for i in range(0,n):
    for j in range(0,i):
        j=j+1
        print(j, end=" ")       
    print("\r")    