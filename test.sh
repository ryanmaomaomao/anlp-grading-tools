docker build . -t anlp
export ANLP_TMP_DIR=/home/hzhu2/anlp-grading-tools/tmp
export SUBMISSION_DIR=/home/hzhu2/minnn-assignment
export DATA_DIR=/home/hzhu2/anlp-grading-tools/data
export SCORES_DIR=/home/hzhu2/anlp-grading-tools/scores
python anlp_grading/main.py
