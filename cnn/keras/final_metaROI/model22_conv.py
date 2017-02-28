from keras.regularizers import l2
from keras.layers import Input, Dense, GaussianNoise, Convolution3D, Flatten, Dropout
from keras.models import Model


def build_model(input_shape=(1, 6, 6, 6), trainable=True):
    name = 'metaROI2'
    do = 1.0/6
    input = Input(shape=input_shape, name=name+'_input')
    x = GaussianNoise(0.001, name=name+'_noise1')(input)
    x = Convolution3D(64, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name=name+'_conv1', trainable=trainable)(x)
    x = Dropout(do, name=name+'_dropout1')(x)
    x = Convolution3D(128, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name=name+'_conv2', trainable=trainable)(x)
    x = Dropout(do, name=name+'_dropout2')(x)
    x = Convolution3D(256, 2, 2, 2, activation='relu', W_regularizer=l2(0.0001), name=name+'_conv3', trainable=trainable)(x)
    x = Dropout(do, name=name+'_dropout3')(x)
    x = Flatten(name=name+'_flatten1')(x)
    return input, x