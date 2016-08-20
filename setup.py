from setuptools import setup

setup(name='jobautomate',
      version='1.0.1',
      author='Mandeep Bhutani',
      packages=['jobautomate', 'jobautomate.tests'],
      install_requires=[
        'indeed',
        'selenium',
        'click',
        'xvfbwrapper'
      ],
      entry_points='''
        [console_scripts]
        jobautomate=jobautomate.commandline:cli
        ''',
      )
