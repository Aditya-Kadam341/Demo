true_tags = ["NN", "DT", "P", "HYP"]
dummy_tags = ["NN", "VB", "P", "P"]
# tp = 0
# tn = 0
# fn = 0
# fp = 0
tag = "P"
# if (len(y_true)) == (len(y_pred)):
#     for i in range(len(y_true)):
#         print(y_true[i],y_pred[i])
#         if (y_true[i] == label ) and (y_pred[i] == label):
#             tp = tp+1
#         elif (y_true[i] == label ) and  (y_pred[i] != label):
#             fn = fn+1
#         elif (y_true[i] != label ) and  (y_pred[i] == label):
#             fp = fp+1
#         elif (y_true[i] != label ) and  (y_pred[i] != label):
#             tn=tn+1
# print(tp,tn,fp,fn)
# print("sum of all",tp+tn+fp+fn)
# Precision = tp/(tp+fp)
# Recall = tp/(tp+fn)
# F1Score= 2*(Precision*Recall)/(Precision + Recall)
# print("Precision of Tag", label, ":",Precision)
# print("Recall of Tag", label, ":",Recall)
# print("F1Score of Tag", label, ":",F1Score)


def matrix_values(y_pred,y_true,label):
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
        # print("True positive",tp)
        # print("False positive",fp)
        # print("False negative",fn)
        # print("True negative",tn)
    return [[true_positive, false_positive],[false_negative,true_negative]]

print(matrix_values(true_tags,dummy_tags,tag))

