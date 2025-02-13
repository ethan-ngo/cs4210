#-------------------------------------------------------------------------
# AUTHOR: Ethan Ngoo
# FILENAME: decision_tree
# SPECIFICATION: Takes in a csv file containing sample data and forms a decision tree.
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('Assignment1/contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
#--> add your Python code here
# X =
for i in range(len(db)):
  newRow = []
  for j in range(len(row)-1):
      if(db[i][j] == "Young" or db[i][j] == "Myope" or db[i][j] == "No" or db[i][j] == "Reduced"):
          newRow.append(1)
      elif(db[i][j] == "Presbyopic" or db[i][j] == "Hypermetrope" or db[i][j] == "Yes" or db[i][j] == "Normal"):
          newRow.append(2)
      else:
          newRow.append(3)
  X.append(newRow)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
#--> addd your Python code here
# Y =
for row in db:
    if row[-1] == "Yes":
      Y.append(1)
    else:
      Y.append(2)
       
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()