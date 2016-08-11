from setuptools import setup

setup(name='jobautomate',
      version='0.9',
      author='Mandeep Bhutani',
      packages=['jobautomate'],
      install_requires=[
        'indeed',
        'selenium',
        'requests',
      ],
      entry_points='''
        [console_scripts]
        jobautomate=jobautomate.commandline:cli
        ''',
      )
