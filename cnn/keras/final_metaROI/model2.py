from keras.regularizers import l2
from keras.layers import Input, Dense, GaussianNoise, Convolution3D, Flatten, Dropout
from keras.models import Model


def build_model(input_shape=(1, 6, 6, 6)):
    name = 'metaROI2'
    do = 1.0/6
    input = Input(shape=input_shape, name=name+'_input')
    x = GaussianNoise(0.001, name=name+'_noise1')(input)
    x = Convolution3D(64, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name=name+'_conv1')(x)
    x = Dropout(do, name=name+'_dropout1')(x)
    x = Convolution3D(128, 3, 3, 3, activation='relu', W_regularizer=l2(0.0001), name=name+'_conv2')(x)
    x = Dropout(do, name=name+'_dropout2')(x)
    x = Convolution3D(256, 2, 2, 2, activation='relu', W_regularizer=l2(0.0001), name=name+'_conv3')(x)
    x = Dropout(do, name=name+'_dropout3')(x)
    x = Flatten(name=name+'_flatten1')(x)

    x = Dense(512, activation='relu', W_regularizer=l2(0.0001), name=name+'_dense1')(x)
    x = Dropout(0.5, name=name+'_dropout4')(x)
    x = Dense(256, activation='relu', W_regularizer=l2(0.0001), name=name+'_dense2')(x)
    x = Dropout(0.5, name=name+'_dropout5')(x)
    x = Dense(128, activation='relu', W_regularizer=l2(0.0001), name=name+'_dense3')(x)
    x = Dropout(0.5, name=name+'_dropout6')(x)

    output = Dense(1, activation='sigmoid', W_regularizer=l2(0.0001), name=name+'_dense4')(x)

    return Model(input=input, output=output)

