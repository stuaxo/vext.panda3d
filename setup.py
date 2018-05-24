#!/usr/bin/env python

from __future__ import print_function

info = """
Allow use of system Panda3D from a virtualenv
Should work on all platforms.

report bugs to https://github.com/stuaxo/vext
"""

version = "0.7.0"
vext_version = "vext>=%s" % version

from glob import glob
from subprocess import call

from setuptools import setup
from setuptools.command.install import install
from setuptools.command.install_lib import install_lib

import sys

vext_files = glob("*.vext")


def _post_install(self):
    cmd = ["vext", "-e", "-i" + (" -i".join(vext_files))]
    call(cmd)


class Install(install):
    def run(self):
        # from pip
        #
        # if ran from some setup.py then vexts own setup will take care of this...
        #
        # TOOD - Move this code to a common place.
        print("vext.gi Install")
        if sys.prefix == '/usr':
            print("Not installing PTH file to real prefix")
            return
        call(["pip", "install", vext_version])
        install.run(self)
        install.execute(self, _post_install, [self], msg="Install vext files:")


setup(
    name='vext.panda3d',
    version=version,
    description='Use system panda3d from a virtualenv',
    long_description=info,

    cmdclass={
        'install': Install,
    },

    url='https://github.com/stuaxo/vext',
    author='Stuart Axon',
    author_email='stuaxo2@yahoo.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='virtualenv panda3d 3d vext',

    setup_requires=["setuptools>=0.18.8"],
    install_requires=[vext_version],
)
