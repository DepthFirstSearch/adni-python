#!/bin/bash

THEANO_FLAGS=device=gpu,floatX=float32,lib.cnmem=1.0 python train_AE_NC_2.py 7 > output_AE_NC_2_CV7
THEANO_FLAGS=device=gpu,floatX=float32,lib.cnmem=1.0 python train_AE_NC_2.py 8 > output_AE_NC_2_CV8
THEANO_FLAGS=device=gpu,floatX=float32,lib.cnmem=1.0 python train_AE_NC_2.py 9 > output_AE_NC_2_CV9
THEANO_FLAGS=device=gpu,floatX=float32,lib.cnmem=1.0 python train_AE_NC_2.py 10 > output_AE_NC_2_CV10

