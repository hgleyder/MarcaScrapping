from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import svm
from sklearn import naive_bayes
from sklearn.feature_extraction.text import TfidfTransformer
from keras import models
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import StratifiedKFold
from keras import layers
import numpy

tfidfconverter = TfidfTransformer()



# Create function returning a compiled network
def create_network():
    f = open('datasets/instances.txt', 'r')
    instances = f.readlines()
    aux = []
    for inst in instances:
        i = inst.replace('\n', "").split(",")
        val = []
        for v in i:
            val.append(int(v))
        aux.append(val)
    instances = aux

    instances = tfidfconverter.fit_transform(instances).toarray()

    input_dim = instances.shape[1]

    # Start neural network
    network = models.Sequential()

    network.add(layers.Dense(5, input_dim=input_dim, activation='relu'))
    network.add(layers.Dense(10, activation='relu'))
    network.add(layers.Dense(1, activation='sigmoid'))

    # Compile neural network
    network.compile(loss='binary_crossentropy',  # Cross-entropy
                    optimizer='adamax',  # Root Mean Square Propagation
                    metrics=['accuracy'])  # Accuracy performance metric

    # Return compiled network
    return network


# # Function to create model, required for KerasClassifier
# def create_model():
#     # create model
#     model = models.Sequential()
#     model.add(layers.Dense(12, input_dim=8, activation='relu'))
#     model.add(layers.Dense(8, activation='relu'))
#     model.add(layers.Dense(1, activation='sigmoid'))
#     # Compile model
#     model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#     return model
#

#============================== CROSS VALIDATION ======================================

def getModelMetrics(model, instances, classes):


    predicted = cross_val_predict(model, instances, classes, cv=10)
    print("================= MODEL SUMMARY =================")
    print(classification_report(classes, predicted))
    print("General Accuracy: " + str(accuracy_score(classes, predicted)))
    print("Correctly Classified Instances: " + str(accuracy_score(classes, predicted) * len(classes)))
    print("Incorrectly Classified Instances: " + str(len(classes) - (accuracy_score(classes, predicted) * len(classes))))
    print("\n*** Confusion Matrix ***")
    cm = confusion_matrix(classes, predicted)
    print("\n  0  1")
    for i in list(range(0, len(cm))):
        print(str(cm[i]) + " " + str(i))
    print("=================================================")


def modelCVEvaluation():
    f = open('datasets/instances.txt', 'r')
    instances = f.readlines()
    aux = []
    for inst in instances:
        i = inst.replace('\n', "").split(",")
        val = []
        for v in i:
            val.append(int(v))
        aux.append(val)
    instances = aux

    instances = tfidfconverter.fit_transform(instances).toarray()
    f = open('datasets/classes.txt', 'r')
    classes = f.readlines()
    aux = []
    for c in classes:
        clase = c.replace('\n', "")
        classIndx = ['positivo', 'negativo']
        aux.append(classIndx.index(clase))
    classes = aux


    neural_network = KerasClassifier(build_fn=create_network, epochs=100, batch_size=10, verbose=False)

    getModelMetrics(neural_network, instances, classes)

modelCVEvaluation()

# # load pima indians dataset
# dataset = numpy.loadtxt("pima-indians-diabetes.data.csv", delimiter=",")
# # split into input (X) and output (Y) variables
# X = dataset[:, 0:8]
# Y = dataset[:, 8]
# # create model
# model = KerasClassifier(build_fn=create_model, epochs=150, batch_size=10, verbose=0)
# # evaluate using 10-fold cross validation
# kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
# results = cross_val_score(model, X, Y, cv=kfold)
# print(results.mean())
