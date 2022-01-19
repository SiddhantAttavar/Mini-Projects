Num=int(input("Enter a five digit number\n"))
D1=(Num/10000)
D2=(Num-D1*10000)/1000
D3=(Num-D1*10000-D2*1000)/100
D4=(Num-D1*10000-D2*1000-D3*100)/10
D5=(Num-D1*10000-D2*1000-D3*100-D4*10)/1

print D1
print D2
print D3
print D4
print D5
