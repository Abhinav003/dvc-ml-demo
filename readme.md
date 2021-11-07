# Reference Repository.
https://github.com/c17hawke/dvc-ML-demo-AIOps

# Steps :

## Step1 :: Create an empty github repository.

## Step2 :: Initialize a git local repo and connect it with remote.
# Open an empty project and follow below command.

git init

## Step3 :: Create and activate environment.
conda create -n dvc_ml python=3.7
conda activate dvc_ml

## Step4 :: Create requirement file and install dependencies.
pip install -r requirements.txt

## Step5 :: Initialize dvc
dvc init

## Step6 :: Create the skeleton directory structure.
# Utility and config folder
mkdir -p src/utils config

## Step7 :: Create a setup file.
touch setup.py
# paste the below content in setup.py file and make necessary changes.
# in requirements.txt add
-e local

## Step8 :: Create the config file.
touch config/config.yaml

## Step9 :: Create the stage01 python file and all_utils.py file.
touch src/stage01_load_save.py src/utils/all_utils.py

# Contents of both the files should be referred.

## Step 19 L Create the dvc.yaml file and add the stage01.
touch dvc.yaml

## Step10 :: Run the dvc command
dvc repro

## Step11 :: Push the changes to remote repository.
git add .
git commit -m "stage 01 added."
git push origin main

