from keras.models import Sequential
from keras.layers.convolutional import Convolution3D
from keras.layers.core import Flatten, Dropout, Dense
from keras.layers.noise import GaussianNoise
from keras.regularizers import l2


def build_model(input_shape=(1, 8, 8, 8)):
	l = 0.0001
	model = Sequential()
        model.add(GaussianNoise(0.001, input_shape=input_shape))
	model.add(Convolution3D(64, 3, 3, 3, activation='relu', border_mode='same', W_regularizer=l2(l)))
        model.add(Dropout(0.1))
	model.add(Convolution3D(128, 3, 3, 3, activation='relu', W_regularizer=l2(l)))
        model.add(Dropout(0.1))
	model.add(Convolution3D(256, 3, 3, 3, activation='relu', W_regularizer=l2(l)))
        model.add(Dropout(0.1))
	model.add(Convolution3D(512, 3, 3, 3, activation='relu', W_regularizer=l2(l)))
        model.add(Dropout(0.1))
        model.add(Convolution3D(1024, 2, 2, 2, activation='relu', W_regularizer=l2(l)))
        model.add(Dropout(0.1))
	model.add(Flatten())

	model.add(Dense(512, activation='relu', W_regularizer=l2(l)))
	model.add(Dropout(0.2))
	model.add(Dense(256, activation='relu', W_regularizer=l2(l)))
	model.add(Dropout(0.2))
	#model.add(Dense(128, activation='relu', W_regularizer=l2(l)))
	#model.add(Dropout(0.2))
	model.add(Dense(2, activation='softmax', W_regularizer=l2(l)))

	return model

