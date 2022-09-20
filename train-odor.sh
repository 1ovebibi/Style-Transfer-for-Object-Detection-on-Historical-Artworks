#!/bin/bash -l
#SBATCH --job-name=train-obj365
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=a100
#Timelimit format: "12:00:00" -- max is 24h
#SBATCH --time=23:30:00


echo "Your job is running on" $(hostname)

module load cuda/11.6.1
source activate py38   

python3 tools/train.py configs/swin/obj365-frcnn.py

echo "FINISHED"