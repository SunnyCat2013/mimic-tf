#import tensorflow as tf
import mimic_tf as tf

'''
implement
 (a * b)/(a + b)
'''


a = tf.constant(5.)
b = tf.constant(15.)

mul = tf.multiply(a, b)

ad = tf.add(a, b)

out = tf.div(mul, ad)


with tf.Session() as sess:
    print('session out:', sess.run(out))
