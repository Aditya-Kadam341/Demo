y_true = ["NN", "DT", "P", "HYP"]
y_pred = ["NN", "VB", "P", "P"]
tp = 0
tn = 0
fn = 0
fp = 0
label = "P"
if (len(y_true)) == (len(y_pred)):
    for i in range(len(y_true)):
        print(y_true[i],y_pred[i])
        if (y_true[i] == label ) and (y_pred[i] == label):
            tp = tp+1
        elif (y_true[i] == label ) and  (y_pred[i] != label):
            fn = fn+1
        elif (y_true[i] != label ) and  (y_pred[i] == label):
            fp = fp+1
        elif (y_true[i] != label ) and  (y_pred[i] != label):
            tn=tn+1
print(tp,tn,fp,fn)
print("sum of all",tp+tn+fp+fn)
Precision = tp/(tp+fp)
Recall = tp/(tp+fn)
F1Score= 2*(Precision*Recall)/(Precision + Recall)
print("Precision of Tag", label, ":",Precision)
print("Recall of Tag", label, ":",Recall)
print("F1Score of Tag", label, ":",F1Score)
