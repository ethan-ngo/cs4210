#-------------------------------------------------------------------------
# AUTHOR: Ethan Ngo
# FILENAME: naive_bayes.py
# SPECIFICATION: Prints instances of naivebayes predictions with confidence >= 0.75
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
#Reading the training data in a csv file
#--> add your Python code here
db = []
with open('Assignment2/weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#Transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = []
for row in db:
   newRow = []
   for i in range(len(row)-1):
      if(row[i] == "Sunny" or row[i] == "Hot" or row[i] == "High" or row[i] == "Strong"):
         newRow.append(1)
      elif(row[i] == "Overcast" or row[i] == "Cool" or row[i] == "Normal" or row[i] == "Weak"):
         newRow.append(2)
      else:
         newRow.append(3)
   X.append(newRow)
   
      
#Transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = [1 if row[-1] == "Yes" else 2 for row in db]

#Fitting the naive bayes to the data
clf = GaussianNB(var_smoothing=1e-9)
clf.fit(X, Y)

#Reading the test data in a csv file
#--> add your Python code here
header = 0
test = []
with open('Assignment2/weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         test.append(row)
      else:
         header = row
#Printing the header of the solution
#--> add your Python code here
print("{:<11} {:<11} {:<11} {:<11} {:<11}".format(header[0], header[1], header[2], header[3], "Confidence"))

#Use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for row in test:
   newRow = []
   for i in range(len(row)-1):
      if(row[i] == "Sunny" or row[i] == "Hot" or row[i] == "High" or row[i] == "Strong"):
         newRow.append(1)
      elif(row[i] == "Overcast" or row[i] == "Cool" or row[i] == "Normal" or row[i] == "Weak"):
         newRow.append(2)
      else:
         newRow.append(3)
   confidence = max(clf.predict_proba([newRow])[0])
   if confidence >= 0.75:
      print("{:<11} {:<11} {:<11} {:<11} {:<11}".format(row[0], row[1], row[2], row[3], confidence))
   
