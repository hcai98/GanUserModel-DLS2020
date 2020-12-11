from setuptools import setup

import os
BASEPATH = os.path.dirname(os.path.abspath(__file__))

setup(name='ganrl-tfv2',
      py_modules=['ganrl-tfv2'],
      install_requires=[
          'tensorflow'
      ],
)
