from setuptools import setup

setup(name='jobautomate',
      version='0.18.9',
      author='Mandeep Bhutani',
      description='Automate a job search with Indeed',
      url='https://github.com/mandeep/Job-Automate',
      packages=['jobautomate', 'jobautomate.tests'],
      license='GPLv3+',
      install_requires=[
        'indeed==0.0.4',
        'selenium==2.53.6',
        'click==6.6',
        'xvfbwrapper==0.2.8'
      ],
      entry_points='''
        [console_scripts]
        jobautomate=jobautomate.commandline:cli
        ''',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
      ]
      )
