#!/bin/bash

#SBATCH --job-name=data
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:4
#Timelimit format: "12:00:00" -- max is 24h
#SBATCH --time=12:00:00

# %x-%j-on-%N

echo "Your job is running on" $(hostname)

echo $TMPDIR

python3 Untitled.py

echo "FINISHED"