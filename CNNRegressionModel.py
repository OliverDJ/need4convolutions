
from DataReader import DataReader
import cv2
from matplotlib import pyplot as plt
import numpy as np
from keras.models import Model, Sequential
from keras.layers import (Dense, GlobalAveragePooling2D, Flatten, Dropout,
                          Reshape, Conv2D, MaxPooling2D)
from keras.applications.vgg16 import VGG16


def plot_training_score(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'valid'], loc='upper right')
    plt.show()

def create_vgg16_model(img_width, img_height):
    base_model = VGG16(input_shape=(img_width, img_height,3),
                       include_top=False, weights='imagenet',
                       input_tensor=None, pooling=None)

    # Freeze all convolutional layers during training
    for layer in base_model.layers:
        layer.trainable = False
    # Add custom layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(64, activation='relu')(x)

    predictions = Dense(4, activation='softmax')(x)
    # The complete model
    model = Model(inputs=base_model.input, outputs=predictions)
    # compile the model
    model.compile(loss="mse",  # or categorical_crossentropy
                  optimizer='adam',
                  metrics=['acc'])
    return model


def save_model(model_save_dir, model_name, model):
    save_path = '{}/{}'.format(model_save_dir, model_name)
    model.save(save_path)


if __name__ == '__main__':
    source_path = 'data'
    model_save_dir = 'models/'

    img_width, img_height = 200, 200
    model = create_vgg16_model(img_width, img_height)

    data_reader = DataReader(source_path)
    train_images, train_labels = data_reader.get_train_data()
    val_images, val_labels = data_reader.get_val_data()
    test_images, test_labels = data_reader.get_test_data()
    np.set_printoptions(suppress=True)

    history = model.fit(
        train_images, train_labels, validation_data=(val_images, val_labels),
        batch_size=16, epochs=10, verbose=1)

    predictions = model.predict(test_images)

    for i in range(len(predictions)):
        print(predictions[i], test_labels[i])

    save_model(model_save_dir, 'shitty_model.h5', model)
