import tensorflow as tf
x = tf.placeholder(tf.float32)

a = tf.constant(32, dtype=tf.float32)
y = tf.placeholder(tf.float32)

z = a * x + y * y
sess = tf.Session()
print(sess.run(z, {x: 2, y: 4}))
print(sess.run(z, {x: [1, 2, 3], y: [2, 3, 4]}))

W = tf.constant([.25], dtype=tf.float32)
b = tf.constant([-.64], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

# init = tf.global_variables_initializer()
# sess.run(init)
print(sess.run(linear_model, {x: [4, 5, 1, 8]}))

sess.close()
