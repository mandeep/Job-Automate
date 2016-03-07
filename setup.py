from setuptools import setup, find_packages

setup(name='jobautomate',
      version='0.0.4',
      author='Mandeep Bhutani',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
        'indeed',
        'selenium',
        'requests==2.0.0',
      ],
      entry_points='''
        [console_scripts]
        jobautomate=jobautomate.commandline:main
        ''',
      )
