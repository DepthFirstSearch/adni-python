from keras.models import Sequential
from keras.layers.convolutional import Convolution3D
from keras.layers.core import Flatten, Dropout, Dense
from keras.layers.noise import GaussianNoise
from keras.regularizers import l2


def build_model(input_shape=(1, 19, 22, 11)):
        name = 'AAL61'
        do = 1.0 / 16
        l = 0.0001
	model = Sequential()
        model.add(GaussianNoise(0.001, input_shape=input_shape, name=name+'_noise1'))
	model.add(Convolution3D(32, 5, 5, 2, activation='relu', W_regularizer=l2(l), name=name+'_conv1'))
        model.add(Dropout(do, name=name+'_dropout1'))
	model.add(Convolution3D(32, 3, 5, 2, activation='relu', W_regularizer=l2(l), name=name+'_conv2'))
        model.add(Dropout(do, name=name+'_dropout2'))
        model.add(Convolution3D(64, 3, 5, 2, activation='relu', W_regularizer=l2(l), name=name+'_conv3'))
        model.add(Dropout(do, name=name+'_dropout3'))
        model.add(Convolution3D(64, 3, 3, 2, activation='relu', W_regularizer=l2(l), name=name+'_conv4'))
        model.add(Dropout(do, name=name+'_dropout4'))
	model.add(Convolution3D(128, 3, 3, 2, activation='relu', W_regularizer=l2(l), name=name+'_conv5'))
        model.add(Dropout(do, name=name+'_dropout5'))
        model.add(Convolution3D(128, 3, 3, 3, activation='relu', W_regularizer=l2(l), name=name+'_conv6'))
        model.add(Dropout(do, name=name+'_dropout6'))
        model.add(Convolution3D(256, 3, 3, 3, activation='relu', W_regularizer=l2(l), name=name+'_conv7'))
        model.add(Dropout(do, name=name+'_dropout7'))
        model.add(Convolution3D(256, 3, 2, 2, activation='relu', W_regularizer=l2(l), name=name+'_conv8'))
        model.add(Dropout(do, name=name+'_dropout8'))
	model.add(Flatten(name=name+'_flatten1'))

	return model

