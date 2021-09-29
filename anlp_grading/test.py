from pathlib import Path
from anlp_grading.utils import execute_cli_timeout, compare_outputs
import os
data_folder = Path('/mnt/data')
student_folder = Path('/mnt/code')
scores_folder = Path('/mnt/scores')

execute_cli_timeout('cd /mnt/code && python3 /mnt/code/setup.py', timeout=1200)
execute_cli_timeout('cp /mnt/data/classifier_orig.py /mnt/code/classifier_orig.py', timeout=600)
execute_cli_timeout(
    'cd /mnt/code && '
    'python3 /mnt/code/classifier.py '
    '--train=/mnt/data/sst-train.txt '
    '--dev=/mnt/data/sst-dev.txt '
    '--test=/mnt/data/sst-test.txt '
    '--dev_out=sst-dev-output.txt '
    '--test_out=sst-test-output.txt ',
    timeout=1200
)
sst_acc = compare_outputs(std="/mnt/data/sst-test.txt", result="/mnt/code/sst-test-output.txt")
execute_cli_timeout(
    'cd /mnt/code && '
    'python3 /mnt/code/classifier_orig.py '
    '--train=/mnt/data/sst-train.txt '
    '--dev=/mnt/data/sst-dev.txt '
    '--test=/mnt/data/sst-test.txt '
    '--dev_out=sst-dev-output-orig.txt '
    '--test_out=sst-test-output-orig.txt ',
    timeout=1200
)
sst_acc_orig = compare_outputs(std="/mnt/data/sst-test.txt", result="/mnt/code/sst-test-output-orig.txt")
execute_cli_timeout(
    'cd /mnt/code && '
    'python3 /mnt/code/classifier.py '
    '--train=/mnt/data/cfimdb-train.txt '
    '--dev=/mnt/data/cfimdb-dev.txt '
    '--test=/mnt/data/cfimdb-test.txt '
    '--dev_out=cfimdb-dev-output.txt '
    '--test_out=cfimdb-test-output.txt ',
    timeout=1200
)
cfimdb_acc = compare_outputs(std="/mnt/data/cfimdb-test-correctlabels.txt", result="/mnt/code/sst-test-output.txt")
execute_cli_timeout(
    'cd /mnt/code && '
    'python3 /mnt/code/classifier_orig.py '
    '--train=/mnt/data/cfimdb-train.txt '
    '--dev=/mnt/data/cfimdb-dev.txt '
    '--test=/mnt/data/cfimdb-test.txt '
    '--dev_out=cfimdb-dev-output.txt '
    '--test_out=cfimdb-test-output-orig.txt ',
    timeout=1200
)
cfimdb_acc_orig = compare_outputs(std="/mnt/data/cfimdb-test-correctlabels.txt", result="/mnt/code/sst-test-output-orig.txt")

print(sst_acc, sst_acc_orig, cfimdb_acc, cfimdb_acc_orig)

with open(scores_folder / os.environ["ANDREW_ID"], "w") as f:
    f.write(f"{sst_acc}\t{sst_acc_orig}\t{cfimdb_acc}\t{cfimdb_acc_orig}")