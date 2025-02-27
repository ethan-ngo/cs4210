#-------------------------------------------------------------------------
# AUTHOR: Ethan Ngo
# FILENAME: decision_tree_2.py
# SPECIFICATION: Tests the accuracy of decision tree based on training tests of increasing size.
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn import tree
import csv

dataSets = ['Assignment2/contact_lens_training_1.csv', 'Assignment2/contact_lens_training_2.csv', 'Assignment2/contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #Reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #Transform the original categorical training features to numbers and add to the 4D array X.
    #For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    for i in range(len(dbTraining)):
        newRow = []
        for j in range(len(dbTraining[0])-1):
            if(dbTraining[i][j] == "Young" or dbTraining[i][j] == "Myope" or dbTraining[i][j] == "No" or dbTraining[i][j] == "Reduced"):
                newRow.append(1)
            elif(dbTraining[i][j] == "Presbyopic" or dbTraining[i][j] == "Hypermetrope" or dbTraining[i][j] == "Yes" or dbTraining[i][j] == "Normal"):
                newRow.append(2)
            else:
                newRow.append(3)
        X.append(newRow)
    #Transform the original categorical training classes to numbers and add to the vector Y.
    #For instance Yes = 1 and No = 2, Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    for row in dbTraining:
        if row[-1] == "Yes":
            Y.append(1)
        else:
            Y.append(2)

    #Loop your training and test tasks 10 times here
    accuracySum = 0
    for i in range (10):

       #Fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=5)
       clf = clf.fit(X, Y)

       #Read the test data and add this data to dbTest
       #--> add your Python code here
       dbTest = []
       with open("Assignment2/contact_lens_test.csv","r") as csvfile:
           reader = csv.reader(csvfile)
           for i, row in enumerate(reader):
               if i > 0: #skipping the header
                   dbTest.append (row)

       true = 0
       for data in dbTest:
            #Transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            numData =[]
            for feature in data:
                if (feature == "Young" or feature == "Myope" or feature == "No" or feature =="Reduced"):
                    numData.append(1)
                elif (feature == "Presbyopic" or feature == "Hypermetrope" or feature == "Yes" or feature == "Normal"):
                    numData.append(2)
                else:
                    numData.append(3)
            numData.pop()

            class_predicted = clf.predict([numData])[0]
            if(data[-1] == "Yes"):
                data[-1] = 1
            else:
                data[-1] = 2


            #Compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if class_predicted == data[-1]:
                true += 1
       accuracy = true/len(dbTest)
       accuracySum += accuracy

           
    #Find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    average = accuracySum/10
    #Print the average accuracy of this model during the 10 runs (training and test set).
    #Your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("final accuracy when training on " + str(ds) + ": " + str(average))



