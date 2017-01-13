import tensorflow as tf
import numpy as np

# Data sets
BREAST_TRAINING = "training_data.csv"
BREAST_TEST = "testing_data.csv"

# Load datasets.
training_set = tf.contrib.learn.datasets.base.load_csv_without_header(
    filename=BREAST_TRAINING,
    target_dtype=np.int,
    features_dtype=np.int)
test_set = tf.contrib.learn.datasets.base.load_csv_without_header(
    filename=BREAST_TEST,
    target_dtype=np.int,
    features_dtype=np.int)

# Specify that all features have real-value data
feature_columns = [tf.contrib.layers.real_valued_column("", dimension=9)]

# Build 3 layer DNN with 10, 20, 10 units respectively.
classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[10, 20, 10],
                                            n_classes=2,
                                            model_dir="/tmp/breast_model")

# Fit model.
classifier.fit(x=training_set.data,
               y=training_set.target,
               steps=2000)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(x=test_set.data,
                                     y=test_set.target)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))

# Classify two new flower samples.
##new_samples = np.array(
##    [[6.4, 3.2, 4.5, 1.5], [5.8, 3.1, 5.0, 1.7]], dtype=float)
##y = list(classifier.predict(new_samples, as_iterable=True))
##print('Predictions: {}'.format(str(y)))

