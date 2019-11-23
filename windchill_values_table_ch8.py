# A program that prins a formatted table of windchill values
# By Gabriela Milillo

#create a helper function to do the math for the program
# v is wind speed MPH
# t is temperatureF
def windchill(v, t):


    windchill = 35.74 + 0.6215 * t - 35.75*(v**0.16) + 0.4275 * t*(v**0.16)
    if v <3: #where 3 is per book:the formula only applies to 3 miles per hour
        return t
    else:
        return windchill

def main():

    #Make our headers
    
    print(26*" ", "{0}".format("Temperatures"))#centeredish by counting spaces 


    #for loop for temperatures
    print("\nMPH|   ", end="")
    for i in range (-20, 61, 10):#to 61 instead of 60 per book, because of 60 is included/stops at 60
        print("{0:3.0f}".format(i,), end="   ")#i is each number temp start with -20, count 3 spaces to print the other number

    print("\n---+" + 55*"-")
    
    
    #for loop wind speed per mph in increments of 5 mph    
    for v in range (0, 55, 5):
        print("\n{0:3.0f}|".format(v,), end="")# match i spacing above matching the MPH column

    #for loop temperature in 10 degrees increments
        for t in range(-20, 61, 10):
            print("{0:6.0f}".format(windchill(v,t)), end="")

main()
