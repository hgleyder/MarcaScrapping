from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import svm
from sklearn import naive_bayes
from sklearn.feature_extraction.text import TfidfTransformer

tfidfconverter = TfidfTransformer()

#============================== CROSS VALIDATION ======================================

def getModelMetrics(model, instances, classes):
    scores = cross_val_score(model, instances,
                             classes, cv=10)
    print("\nCross Validation Accuracy: %0.2f (+/- %0.2f)\n" % (scores.mean(), scores.std() * 2))

    predicted = cross_val_predict(model, instances, classes, cv=10)
    print "================= MODEL SUMMARY ================="
    print classification_report(classes, predicted)
    print "General Accuracy: " + str(accuracy_score(classes, predicted))
    print "Correctly Classified Instances: " + str(accuracy_score(classes, predicted) * len(classes))
    print "Incorrectly Classified Instances: " + str(len(classes) - (accuracy_score(classes, predicted) * len(classes)))
    print "\n*** Confusion Matrix ***"
    cm = confusion_matrix(classes, predicted)
    print "\n  0  1"
    for i in list(range(0, len(cm))):
        print str(cm[i]) + " " + str(i)
    print "================================================="


def modelCVEvaluation():
    f = open('datasets/instances.txt', 'r')
    instances = f.readlines()
    aux = []
    for inst in instances:
        i = inst.replace('\n', "").split(",")
        i = map(lambda x: float(x), i)
        aux.append(i)
    instances = aux

    instances = tfidfconverter.fit_transform(instances).toarray()
    f = open('datasets/classes.txt', 'r')
    classes = f.readlines()
    aux = []
    for c in classes:
        aux.append(c.replace('\n', ""))
    classes = aux

    # clf = svm.NuSVC()
    clf = svm.LinearSVC()
    # clf = naive_bayes.MultinomialNB()
    getModelMetrics(clf, instances, classes)

modelCVEvaluation()