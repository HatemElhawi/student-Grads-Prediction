import pandas as pd
from sklearn import linear_model
import numpy as np
import csv
import matplotlib.pyplot as plt




df = pd.read_csv('grade19.csv')  #read exel sheet

reg = linear_model.LinearRegression()
reg.fit(df[['7th','12th','att']],df.final) #predect final grade




numOfStudents=int(input("enter number of student"))
print("7th 12th Attendance")



for i in range(numOfStudents):
    mid1, mid2,att = map(int, input("").split())
    output=reg.predict([[mid1, mid2,att]])
    sum=mid1+mid2+att


    if (sum <= 60 ) :
        print("your grade before final exam is " , sum)
        print("the final mark will be  ", np.round(output,2) , "the garde will be " ,end="")



        finalgrade = output
        mark = output
        fields=[mid1,mid2,att,np.round(output,2)]
        with open(r'grade20.csv', 'a+') as f:
            writer = csv.writer(f)
            writer.writerow(fields)



        if (95 <= mark <= 100):
            print("A+")
        elif (90 <= mark < 95):
            print("A")
        elif (85 <= mark < 90):
            print("A-")
        elif (80 <= mark < 85):
            print("B+")
        elif (75 <= mark < 80):
            print("B")
        elif (70 <= mark < 75):
            print("B-")
        elif (65 <= mark < 70):
            print("C+")
        elif (60 <= mark < 65):
            print("C")
        elif (60 <= mark < 50):
            print("D")
        elif ( mark > 101):
            print("please enter valid input")
        else:
            print("F")
        print("7th 12th Attendance")
    else:
        print("Error!!! ",  end="\n")

x1 = np.array([0,25,50,75,100])
y1 = np.array([10,80,25,60,80])
x2 = np.array([0,20,40,60,80,100])
y2 = np.array([70,90,20,30,50,70])
plt.plot(x1,y1,c="g")
plt.plot(x2,y2,c="r")
#plt.show()
dff = pd.read_csv('grade20.csv')
print("2020",round(dff.describe(),1))

