import numpy as np
import heapq as hq
from numpy.random import shuffle
import scipy.spatial.distance as sp
from collections import Counter
from nltk.compat import raw_input
from numpy import *
from DataReadEnumerate import *
from ClassLabel import *

class KNN():

    index_picked=[]

    def calcAccuracy(self,original_class,predicted_class):

        #calculate accuracy
        TP=0
        FN=0
        FP=0
        TN=0

        for i in range(0,len(original_class)):
            if original_class[i] == predicted_class[i]:
                TP += 1
                TN += 1

            else:
                if groupClasses(original_class[i]) == groupClasses(predicted_class[i]):
                    TP += 1
                    TN += 1
                else:
                    FN += 1
                    FP += 1

        print("The number of records classified as true positive is:",TP)
        print("The number of records classified as true negative is:",TN)
        print("The number of records classified as false negative is:",FN)
        print("The number of records classified as false positive is:",FP)
        print("The Accuracy of k-NN Classifier is %.2f" % round((TP/float(len(original_class))) * 100.0,2))


    def randomSampling(self):

        data_set=[]

        filename = "kddcup.data_10_percent_corrected"


        #filename="corrected_test_withLabel"

        with open(filename, 'r') as f:
            tot_data = csv.reader(f, delimiter=',')
            for each_row in tot_data:
                data_set.append(each_row)
            f.close()

        #print("data_set",data_set)

        for i in range(0,5):
            random.shuffle(data_set)

        KNN().getClassLabel(data_set)

        return data_set[:5000]


    def euclideanDistance(self):

        k=raw_input("Enter the k for the k-NN algorithm:")

        master_dict={}

        assigned_label=[]

        calculated_label=[]

        data_set=KNN().randomSampling()

        print("Read the dataset after random sampling",len(data_set))

        assigned_label=KNN().getClassLabel(data_set)

        extracted_data=open_file(data_set)

        data_set_whole=[]

        columns=[0,1,2,3,4,5,11,22,23,32,36,40,41]

        for each in extracted_data:
            list=[]
            for column in columns:
                list.append(each[column])
            data_set_whole.append(list)


        print("Read the dataset after enumeration",len(data_set))

        count=0
        for each in data_set:
            count+=1
            print("Examining",count)
            master_dict={}
            for other in data_set:
                if each != other:
                    distance=sp.euclidean(each,other)
                    master_dict[distance]=other

            distance_list=[]
            #get the one with the least distance
            for key in master_dict.keys():
                distance_list.append(key)

            #getting 1 nearest neighbour
            if int(k) == 1:

                min_distance=min(distance_list)

                neighbour=master_dict.get(min_distance)

                m=0
                #get the index of the class label of the nearest neighbour
                for i in range(0,len(data_set)):
                    if neighbour == data_set[i]:
                        m=i
                        break;

                #get the class label from the class label list
                class_label=assigned_label[i]
                calculated_label.append(class_label)

            else:

                #getting k nearest neighbour

                k_min_dist=[]
                for vary in range(0,int(k)):
                    if len(distance_list) != 0:
                        minimum=min(distance_list)
                        k_min_dist.append(minimum)
                        distance_list.remove(minimum)

                #print("k min dist",k_min_dist)

                match_list=[]
                index_list=[]
                for each in k_min_dist:
                    vector=master_dict.get(each)
                    match_list.append(vector)


                for i in range(0,len(match_list)):
                    for j in range(0,len(data_set)):
                        if data_set[j] == match_list[i]:
                            index_list.append(j)

                class_labels=[]
                for index in index_list:
                    class_labels.append(assigned_label[index])

                count_new=Counter(class_labels)

                label=count_new.most_common()[0]

                calculated_label.append(label[0])


        #print("calculated_label",calculated_label)
        #print("assigned label",assigned_label)

        #for i in range(0,len(class_name_list)):

        print("Labels calculated")

        #count=0
        #for i in range(0,len(calculated_label)):
            #if calculated_label[i] == assigned_label[i]:
                #count+=1
        #print("accuracy count",count)


        KNN().calcAccuracy(assigned_label,calculated_label)


    def getClassLabel(self,data_read):

        class_label=[]

        for each in data_read:
            class_label.append(each[41])

        #print("class label",class_label)

        return class_label

KNN().euclideanDistance()