#!/bin/bash --login
#$ -cwd
#SBATCH --job-name=grade_test
#SBATCH --out=base_model.out.%J
#SBATCH --err=base_model.err.%J
#SBATCH --nodes=1
#SBATCH -p cpu_small
#SBATCH --mail-type=all
#SBATCH --mail-user=cot13@aber.ac.uk

conda activate AI_SUM

python BruteForce.py


