#!/bin/sh
train=../mf-train
predict=../mf-predict

##########################################################################
# Build package if no binary found and this script is exectuted via the
# following command.
#  libmf/demo > sh demo.sh
##########################################################################
if [ ! -s $train ] || [ ! -s $predict ]
then
    (cd .. && make)
fi

##########################################################################
# Real-valued matrix factorization (RVMF)
##########################################################################
echo "--------------------------------"
echo "Real-valued matrix factorization"
echo "--------------------------------"
# In-memory training with holdout valudation
$train -f 0 -l2 0.05 -k 100 -t 10 -p netflix_test.te.txt netflix_train.tr.txt rvmf_model.txt
# Do prediction and show MAE
$predict -e 1 netflix_test.te.txt rvmf_model.txt rvmf_output.txt
