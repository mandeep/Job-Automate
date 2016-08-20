from setuptools import setup

setup(name='jobautomate',
      version='1.0.1',
      author='Mandeep Bhutani',
      packages=['jobautomate', 'jobautomate.tests'],
      license='GPLv3+',
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
      classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
      ]
      )
