import random

from cnn.keras import callbacks
from cnn.keras.auto_test.model import build_model
from cnn.keras.optimizers import load_config, MySGD
from cnn.keras.auto_test.image_processing import inputs
from utils.load_scans import load_scans
from utils.sort_scans import sort_subjects
from utils.split_scans import read_imageID
import sys
sys.stdout = sys.stderr = open('output_1', 'w')


# Training specific parameters
target_size = (21, 21, 21)
FRACTION_TRAIN = 0.8
SEED = 42  # To deactivate seed, set to None
classes = ['Normal', 'AD']
batch_size = 16
load_all_scans = True
num_epoch = 2000
# Number of training samples per epoch
num_train_samples = 830
# Number of validation samples per epoch
num_val_samples = 449
# Paths
path_ADNI = '/home/mhubrich/ADNI_intnorm_auto_npy'
path_checkpoints = '/home/mhubrich/checkpoints/adni/auto_test_1'
path_weights = None
path_optimizer_weights = None
path_optimizer_updates = None
path_optimizer_config = None


def _split_scans():
    scans = load_scans(path_ADNI)
    subjects, names_tmp = sort_subjects(scans)
    scans_train = []
    scans_val = []
    groups = {}
    for c in classes:
        groups[c] = []
    for n in names_tmp:
        if subjects[n][0].group in classes:
            groups[subjects[n][0].group].append(n)
    min_class = 999999
    for c in groups:
        if len(groups[c]) < min_class:
            min_class = len(groups[c])
    random.seed(SEED)
    for c in groups:
        random.shuffle(groups[c])
        count = 0
        for n in groups[c]:
            for scan in subjects[n]:
                if count < FRACTION_TRAIN * len(groups[c]) and count < FRACTION_TRAIN * min_class:
                    scans_train.append(scan)
                else:
                    scans_val.append(scan)
            count += 1
    return scans_train, scans_val


def train():
    # Get inputs for training and validation
    scans_train = read_imageID(path_ADNI, 'train_set')
    scans_val = read_imageID(path_ADNI, 'val_set')
    train_inputs = inputs(scans_train, target_size, batch_size, load_all_scans, classes, 'train', SEED)
    val_inputs = inputs(scans_val, target_size, batch_size, load_all_scans, classes, 'val', SEED)

    # Set up the model
    model = build_model(2, input_shape=(128,)+target_size)
    config = load_config(path_optimizer_config)
    if config == {}:
        config['lr'] = 0.001
        config['decay'] = 0.000001
        config['momentum'] = 0.9
    sgd = MySGD(config, path_optimizer_weights, path_optimizer_updates)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    if path_weights:
        model.load_weights(path_weights)

    # Define callbacks
    cbks = [callbacks.checkpoint(path_checkpoints),
            callbacks.save_optimizer(sgd, path_checkpoints, save_only_last=True),
            callbacks.batch_logger(27),
            callbacks.print_history()]

    # Start training
    hist = model.fit_generator(
        train_inputs,
        samples_per_epoch=train_inputs.nb_sample,
        nb_epoch=num_epoch,
        validation_data=val_inputs,
        nb_val_samples=val_inputs.nb_sample,
        callbacks=cbks,
        verbose=2,
        max_q_size=16,
        nb_worker=1,
        pickle_safe=True)

    return hist


if __name__ == "__main__":
    hist = train()
