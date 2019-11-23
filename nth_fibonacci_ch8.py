# A program to calculate the nth spot in the Fibonacci
# Per assignment in the book we start at 1 instead of which is the result of 0 plus 1
# by Gabriela Milillo


def main():
    n= int(input("Enter a a spot in the Fibonacci sequence: "))#variable n is the user input
#per the book Fibonacci sequence starts at 1, otherwise it'll be num1=0
    num1=1 #first spot in the seq
    num2=1 #second spot in the seq

#run the loop n times, n is the spot in the Fibonacci sequence
    for i in range(2,n): #the second spot 
        #print for testing
        print("num1 = " + str(num1))
        print("num2 = " + str(num2))

#assigning the sum of the next spot in the sequence        
        sum = num1 + num2
        print("sum = " + str(sum))

#the new num1 now equals num2 in the Fibonacci sequence
        num1=num2
        print()

#the new num2 now equals the sum of num1 + num2 in the Fibonacci sequence
        num2=sum
        print()
        
#output of what the number in that spot in the Fibonacci sequence is
    print("the "+ str(n)+"th/nth spot in the seq. is "+ str(num2))

main()
