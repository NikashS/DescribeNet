# DescribeNet

Part of 4th year thesis research project with Professor Vicente Ordonez-Roman. 

This website is hosted on Heroku at [this link](https://describenet.herokuapp.com/).

## Overview

DescribeNet is a Django app to label ImageNet classes with descriptive captions. These labels are to be used for zero-shot learning (computer vision classification without training on image classes). 

Specifically, these labels will be used as class inputs for CLIP (a state-of-the-art OpenAI model for zero-shot learning on a wide range of datasets). My research code for interacting with CLIP can be found [here](https://github.com/NikashS/VisionResearch).

## Getting started

Install necessary python requirements from `requirements.txt`.

Run `python manage.py runserver` to run the project locally.