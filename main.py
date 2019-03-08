# This file is the lower-level approach to digit recognition.
# The inputted value to predict are preset images.
# The user will simply tell the model which image to predict based
# on the array of preset images.

# This algorithm will use linear support vector machine classification (SVM),
# In SVM the dataset is represented as points in space

# importing data set
from sklearn.datasets import load_digits
from sklearn import svm
import matplotlib.pyplot as plt

print("Loading dataset...")
digits = load_digits()

# data set is organized so that the last digit in the array value matches the actual number on the image
# thus [1] = 1, [21] = 1, [33] = 3, [68] = 8 ...
plt.gray()
plt.matshow(digits.images[23])
plt.show()

# will show the actual 8x8 image
print(digits.images[23])

clf = svm.SVC()

# model training
clf.fit(digits.data[:-1], digits.target[:-1])

# model testing
prediction = clf.predict(digits.data[23:24])

#will then print out, to the console, the predicted value of the inputted image number
print("Predicted Digit: ", prediction)
