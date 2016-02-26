from setuptools import setup, find_packages

setup(name='jobautomate',
      version='0.0.2',
      author='Mandeep Bhutani',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
        'indeed',
        'selenium',
        'requests',
      ],
      entry_points='''
        [console_scripts]
        jobautomate=commandline:main
        ''',
      )
