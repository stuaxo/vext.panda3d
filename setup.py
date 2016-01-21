#!/usr/bin/env python
info="""
Allow use of system Panda3D from a virtualenv
Should work on all platforms.

report bugs to https://github.com/stuaxo/vext
"""


from glob import glob
from subprocess import call

from setuptools import setup
from setuptools.command.install import install

vext_files = glob("*.vext")

def _post_install():
    cmd = ["vext", "-i" + (" -i".join(vext_files))]
    call(cmd)

class Install(install):
    def run(self):
        import sys
        self.do_egg_install()
        self.execute(_post_install, [], msg="Install vext files:")

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
