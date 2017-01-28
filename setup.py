from setuptools import setup

from competitionToolbox.version import __version__


setup(name='quantquestToolbox',
      version=__version__,
      description='The Toolbox for Quant Quest competition',
      url='https://quant-quest.auquan.com',
      author='Auquan',
      author_email='info@auquan.com',
      license='MIT',
      packages=['competitionToolbox'],
      scripts=['problem2.py', 'problem3.py'],
      include_package_data = True,

      install_requires=[
        'auquanToolbox',
        'pandas',
        'numpy',
        'matplotlib',
      ],

      zip_safe=False,
     )