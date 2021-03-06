# Copyright 2013 Blue State Digital
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
from setuptools import setup, find_packages

version = '2'
README = os.path.join(os.path.dirname(__file__), 'README')
long_description = 'Command line client for making API calls.'

setup(
    name='bsdapi',
    version=version,
    description=long_description,
    author='Blue State Digital',
    author_email='help@bluestatedigital.com',
    packages=['bsdapi'],
    package_dir={'bsdapi': 'bsdapi'},
    entry_points={
      'console_scripts': [
            'bsdapi = bsdapi.Main:Cli'
        ]
      },
    license = "Apache",
    keywords = "API, Client, HTTP",
    url = "http://tools.bluestatedigital.com/",
    classifiers=[
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Natural Language :: English",
      ],
    install_requires = ["requests"]
    )
