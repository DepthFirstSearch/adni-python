from keras.models import Sequential
from keras.layers.convolutional import Convolution3D
from keras.layers.core import Flatten, Dropout, Dense
from keras.layers.noise import GaussianNoise
from keras.regularizers import l2


def build_model(input_shape=(1, 21, 21, 21)):
        model = Sequential()
        model.add(GaussianNoise(0.001, input_shape=input_shape, name='AAL65_noise1'))
	model.add(Convolution3D(32, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv1'))
        model.add(Dropout(0.05, name='AAL65_dropout1'))
	model.add(Convolution3D(32, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv2'))
        model.add(Dropout(0.05, name='AAL65_dropout2'))
        model.add(Convolution3D(64, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv3'))
        model.add(Dropout(0.05, name='AAL65_dropout3'))
        model.add(Convolution3D(64, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv4'))
        model.add(Dropout(0.05, name='AAL65_dropout4'))
	model.add(Convolution3D(128, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv5'))
        model.add(Dropout(0.05, name='AAL65_dropout5'))
	model.add(Convolution3D(128, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv6'))
        model.add(Dropout(0.05, name='AAL65_dropout6'))
        model.add(Convolution3D(256, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv7'))
        model.add(Dropout(0.05, name='AAL65_dropout7'))
        model.add(Convolution3D(256, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv8'))
        model.add(Dropout(0.05, name='AAL65_dropout8'))
        model.add(Convolution3D(512, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv9'))
        model.add(Dropout(0.05, name='AAL65_dropout9'))
        model.add(Convolution3D(512, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name='AAL65_conv10'))
        model.add(Dropout(0.05, name='AAL65_dropout10'))
	model.add(Flatten(name='AAL65_flatten1'))

        model.add(Dense(256, activation='relu', W_regularizer=l2(0.0001), name='AAL65_dense1'))
        model.add(Dropout(0.2, name='AAL65_dropout11'))
        model.add(Dense(128, activation='relu', W_regularizer=l2(0.0001), name='AAL65_dense2'))
        model.add(Dropout(0.2, name='AAL65_dropout12'))
        model.add(Dense(2, activation='softmax', W_regularizer=l2(0.0001), name='AAL65_dense3'))

	return model

