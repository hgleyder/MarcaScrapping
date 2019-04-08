from ModelConstructor import *
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB,MultinomialNB



#============================== CROSS VALIDATION ======================================

# =========================== PRINCIPAL MODEL =========================================

# model = CreatePrincipalClassificationModel()
# instancias =  getModelInstancesAttributes("PrincipalModel/instances.txt")
# classes = getModelInstancesClasses("PrincipalModel/classes.txt")
# predicted = cross_val_predict(model,instancias,classes,cv=10)
# print "================= MODEL SUMMARY ================="
# print classification_report(classes,predicted)
# print "General Accuracy: " +str(accuracy_score(classes,predicted))
# print "Correctly Classified Instances: "+ str(accuracy_score(classes,predicted)*len(classes))
# print "Incorrectly Classified Instances: "+ str(len(classes) - (accuracy_score(classes,predicted)*len(classes)))
# print "\n*** Confusion Matrix ***"
# for i in list(range(0,len(model.classes_))):
#     print str(i)+": "+ model.classes_[i]
# cm =confusion_matrix(classes,predicted)
# print "\n  0  1  2"
# for i in list(range(0,len(cm))):
#     print str(cm[i])+" "+str(i)
# print "================================================="


# =========================== ANGUSTIA MODEL =========================================


model = CreateAngustiaClassificationModel()
scores = cross_val_score(model, getModelInstancesAttributes("AngustiaModel/instances.txt"), getModelInstancesClasses("AngustiaModel/classes.txt"), cv=10)
print("\nCross Validation Accuracy: %0.2f (+/- %0.2f)\n" % (scores.mean(), scores.std() * 2))
instancias =  getModelInstancesAttributes("AngustiaModel/instances.txt")
classes = getModelInstancesClasses("AngustiaModel/classes.txt")
predicted = cross_val_predict(model,instancias,classes,cv=10)
print "================= MODEL SUMMARY ================="
print classification_report(classes,predicted)
print "General Accuracy: " +str(accuracy_score(classes,predicted))
print "Correctly Classified Instances: "+ str(accuracy_score(classes,predicted)*len(classes))
print "Incorrectly Classified Instances: "+ str(len(classes) - (accuracy_score(classes,predicted)*len(classes)))
print "\n*** Confusion Matrix ***"
for i in list(range(0,len(model.classes_))):
    print str(i)+": "+ model.classes_[i]
cm =confusion_matrix(classes,predicted)
print "\n  0  1  2"
for i in list(range(0,len(cm))):
    print str(cm[i])+" "+str(i)
print "================================================="