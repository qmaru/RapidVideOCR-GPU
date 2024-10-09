# -*- encoding: utf-8 -*-
import setuptools

MODULE_NAME = "rapid_videocr"


setuptools.setup(
    name=MODULE_NAME,
    version="1.0.0",
    platforms="Any",
    description="Tool for extracting hard subtitles from videos.",
    author="qmaru",
    url="https://github.com/qmaru/RapidVideOCR-GPU.git",
    license="Apache-2.0",
    include_package_data=True,
    install_requires=[
        "tqdm",
        "rapidocr_paddle",
        "paddlepaddle-gpu @ https://www.paddlepaddle.org.cn/packages/stable/cu123/",
    ],
    packages=[MODULE_NAME],
    package_data={"": ["*.yaml"]},
    keywords=["rapidocr,videocr,subtitle"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6,<3.12",
    entry_points={
        "console_scripts": [f"{MODULE_NAME}={MODULE_NAME}.main:main"],
    },
)
