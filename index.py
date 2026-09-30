list_data=[2,9,11,-2,8,13,14,90]
new_list=list_data[::2]
new_list_2=list_data[1::2]
print(sum(new_list))
print(sum(new_list_2))


first_sum,second_sum=0,0

index=0
while index<len(list_data):
    if index %2==0:
        first_sum+=list_data[index]
    else:
        second_sum+=list_data[index]
    index+=1
print(first_sum) #next topic pen
print(second_sum)        

for num in range(10):
    if num>5:
        print("terminated")
        break
    print(num)

for num in range (10):
  if num%2==0:
       print("skipped")
       continue
  print(num)

a=input("enter the 1st input\n")
b=input("enter the 2nd input\n")     
c=input("enter the 3rd input\n")
a,b,c=int(a),int(b),int(c)
print(a,b,c)

# a=input("enter the 1st input\n")
# b=input("enter the 2nd input\n")     
# c=input("enter the 3rd input\n")
# print(a + b + c)


