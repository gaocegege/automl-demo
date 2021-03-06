import tensorflow as tf
mnist = tf.keras.datasets.mnist

flags = tf.app.flags
flags.DEFINE_string("optimizer", "adam", "optimizer")
flags.DEFINE_string("data_dir", "/tmp/mnist.npz",
"Directory for storing mnist data")

FLAGS = flags.FLAGS

print("data_dir:", FLAGS.data_dir)
print("optimizer:", FLAGS.optimizer)

(x_train, y_train),(x_test, y_test) = mnist.load_data(FLAGS.data_dir)
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=FLAGS.optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1)
loss, acc = model.evaluate(x_test, y_test)
print("accuracy:{}".format(acc))
print("loss:{}".format(loss))
