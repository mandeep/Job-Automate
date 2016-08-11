from setuptools import setup

setup(name='jobautomate',
      version='0.9',
      author='Mandeep Bhutani',
      packages=['jobautomate', 'jobautomate.tests'],
      install_requires=[
        'indeed',
        'selenium',
        'click'
      ],
      entry_points='''
        [console_scripts]
        jobautomate=jobautomate.commandline:cli
        ''',
      )
