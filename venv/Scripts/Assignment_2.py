#Group A2_Team03
#Names: Sarthak Satish Bhingarde, Bhairavi Jitendra Jadhav

max_year = 0
max_time = 0
max_speed = 0
landfall = []
d = {}
cat1=0
cat2=0
cat3=0
cat4=0
cat5=0
f=False

def maxWind(x, y, z):                                                          #This function calculates the max value of wind speed
    
    global max_speed
    if (int(z) >= int(max_speed)):
        global max_year
        max_year= x
        global max_time
        max_time = y
        max_speed = z

fileopen=['hurdat2-1851-2019-052520.txt','hurdat2-nepac-1949-2019-042320.txt']      #Creating a list of files to iterate through both the files
dict={}
for q in fileopen:
    with open(q, 'r') as f:
        for line in f:
            values=line.split(',')
            if not (line.startswith('AL') | line.startswith('EP') | line.startswith('CP')):     #Comparing line starts for both files
                year=values[0]
                time=values[1]
                speed=values[6]
                if values[2].strip() == 'L':                                                    #stripping blank spaces for comparing L
                    landfall.append(values[2])
                maxWind(year,time,speed)                                                        #passing year time and speed to maxWind()
            else:
                if f == True:                                                                   #if statement is for skipping first execution
                    print(max_year, max_time, max_speed,end=" ")

                    y=str(max_year)                                                        #Converting max_year to string from int for concatenation
                    z=y[0:4]
                    if z in d.keys() :                                                          #Adding keys and values if not present in dictionary
                        d[z].append(int(max_speed))                                             #and appending values if key already present
                    else :
                        m_speed = [int(max_speed)]
                        d[z] = m_speed

                    if len(landfall) > 0:                                                       #landfall is a list for calculating value of L
                        print("yes")
                    else:
                        print()
                id=values[0]
                name=values[1]
                max_year = 0
                max_time=0
                max_speed=0
                f=True
                print(id,name)
                landfall=[]
    print(max_year, max_time, max_speed)                                                       #this is for printing the last iteration as
    if z in d.keys():                                                                          #as the loop won't go into else for last iteration
        d[z].append(int(max_speed))
    else:
        m_speed = [int(max_speed)]
        d[z] = m_speed

print("Year Storms Cat1 Cat2 Cat3 Cat4 Cat5")

for i in d.keys():                                                                 #iterating through the keys in the dictionary
    length_key=len(d[i])                                                           #calculating the dictionary length of "values" which is a list
    print(i,str(length_key).rjust(5),end=" ")
    a=d[i]                                                                      #adding list elements in a for categorizing according to storm speeds
    for k in a:
        p=int(k)
        if(p > 137):
            cat5=cat5+1
        elif(p>113):
            cat4=cat4+1
        elif(p>96):
            cat3=cat3+1
        elif(p>83):
            cat2=cat2+1
        elif(p>64):
            cat1=cat1+1

    print(str(cat1).rjust(4),end=" ")
    print(str(cat2).rjust(4),end=" ")
    print(str(cat3).rjust(4),end=" ")
    print(str(cat4).rjust(4),end=" ")
    print(str(cat5).rjust(4))
    cat1=0
    cat2=0
    cat3=0
    cat4=0
    cat5=0