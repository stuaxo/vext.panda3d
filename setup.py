import os

from distutils import sysconfig
from setuptools import setup
from setuptools.command.install import install

here=os.path.dirname(os.path.abspath(__file__))
site_packages_path = sysconfig.get_python_lib()


class CheckInstall(install):
    def run(self):
        # TODO - massive memory leak happens here !
        self.do_egg_install()
 
long_description="""
Allow use of system Panda3d in a virtualenv  
Should work on all platforms.
"""

setup(
    name='vext.panda3d',
    version='0.2.1',
    description='Use system panda3d from a virtualenv',
    long_description=long_description,

    cmdclass={
        'install': CheckInstall,
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

    install_requires=["vext"],

    # Install pygtk vext
    data_files=[
        (os.path.join(site_packages_path, 'vext/specs'), ['panda3d.vext'])
    ],
)
