#import tensorflow as tf
import mimic_tf as tf

'''
- forward Done 2021.09.16 12:03
- backward
- Dense layer
'''

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



