import os
# Import V1 compatibility of TenserFlow
import tensorflow.compat.v1 as tf
# Disabling V2 behavior
tf.disable_v2_behavior()

# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define computational graph
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

addition = tf.add(X, Y, name="addition")

# Create the session
with tf.Session() as session :
    result = session.run(addition, feed_dict={X:[1], Y:[4]})
    print(result)
# You'll get a warning message explaining that this is deprecated and that "non-resource variables are not supported in the long term"
# but it will work
