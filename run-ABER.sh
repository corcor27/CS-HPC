#!/bin/bash --login
#$ -cwd
#SBATCH --job-name=grade_test
#SBATCH --out=base_model.out.%J
#SBATCH --err=base_model.err.%J
#SBATCH --gres=gpu:1
#SBATCH -p gpusmall
#SBATCH --mail-type=all
#SBATCH --mail-user=cot12@aber.ac.uk

conda activate /impacs/cot12/anaconda3/MSD

python guobins_test.py


