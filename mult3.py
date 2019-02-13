#!/usr/bin/python3

inp =  input().split()

i = int(inp[0])
n = int(inp[1])

while i <= n:
	t = bin(i)[2:]
	t3 = bin(3*i)[2:]
	print('{:>8}'.format("00" + t) )
	print('{:>8}'.format(t3)     + "\n")
	i+=1

