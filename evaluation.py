########## Temporary Data ##########

true_tags = ["NN", "DT", "P", "HYP"] #correct(GoldStandard data)
dummy_tags = ["NN", "VB", "P", "P"]  #predicted(Dummy data)
tag = "P" # Single label

########## Temporary Data ##########

########## Function to get tp,fp,fn,tn values ##########

def matrix_values(y_pred,y_true,label):
    # initialize variables 
    true_positive = 0
    true_negative = 0
    false_negative = 0
    false_positive = 0
    if (len(y_true)) == (len(y_pred)):
        for i in range(len(y_true)):
            if (y_true[i] == label ) and (y_pred[i] == label):
                true_positive = true_positive+1
            elif (y_true[i] == label ) and  (y_pred[i] != label):
                false_negative = false_negative+1
            elif (y_true[i] != label ) and  (y_pred[i] == label):
                false_positive = false_positive+1
            elif (y_true[i] != label ) and  (y_pred[i] != label):
                true_negative=true_negative+1
    else:
        print("******\nTHE LENGTH OF CORRECT and PREDICTED LIST IS DIFFERENT\n*****")
    # print("True positive1",true_positive)
    # print("False positive1",false_positive)
    # print("False negative1",false_negative)
    # print("True negative1",true_negative)
    return [[true_positive, false_positive],[false_negative,true_negative]]

########## Function to get tp,fp,fn,tn values ##########

# print(matrix_values(true_tags,dummy_tags,tag))

def calculate_precision_recall(y_pred,y_true,label):
    values = matrix_values(y_pred,y_true,label)
    Precision = values[[0][0]][0]/(values[[0][0]][0]+values[[0][0]][1])
    Recall = values[[0][0]][0]/(values[[0][0]][0]+values[[1][0]][0])
    # print("True negative",values[[1][0]][1])
    return Precision,Recall

# print(calculate_precision_recall(true_tags,dummy_tags,tag))

def calculate_f1score(y_pred,y_true,label):
    Precision,Recall = calculate_precision_recall(y_pred,y_true,label)
    F1_Score= 2*(Precision*Recall)/(Precision + Recall)
    return F1_Score

print(calculate_f1score(true_tags,dummy_tags,tag))


