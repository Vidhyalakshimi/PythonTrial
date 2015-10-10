
N = int(input("Enter N: "))

num = []

for i in range(N):
	num.append(int(input()))

print ("Sum: " + str(sum(num)))
print ("Max: " + str(max(num)))