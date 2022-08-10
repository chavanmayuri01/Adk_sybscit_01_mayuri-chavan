# program tp display the fibonacci sequence up to n-th term where n is provided
# change this value for a different result
nterms = 10

# uncomment to take input from the user
# nterms = int(input("how many terms?"))
# first two terms
n1=0
n2=1
count=2
# check if the number of terms is valid
if nterms<=0:
    print("please enter a positive integer:")
elif nterms==1:
    print("fibonnaci sequence upto",nterms,":")
    print(n1)
else:
    print("fibonnaci sequence upto",nterms,":")
    print(n1,",",n2,',')
    while count < nterms:
        nth = n1+n2
        print (nth, ' , ')
        # update values
        n1 = n2
        n2 = nth
        count += 1
