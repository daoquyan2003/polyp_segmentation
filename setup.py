#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    description=("Polyp segmentation training pipeline based on PyTorch Lightning and Hydra"),
    author="Quy-An Dao",
    author_email="daoquyan26122003@gmail.com",
    url="https://github.com/daoquyan2003/polyp_segmentation",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "train_command = src.train:main",
            "eval_command = src.eval:main",
        ]
    },
)
