from setuptools import setup, find_packages

setup(name='file-downloader',
      version='1.0.0',
      description="File Downloader (HTTP, FTP)",
      long_description=open('README.md').read(),
      packages=find_packages(exclude="tests"),
      package_data={
          'agoda': ['log/config.yaml']
      },
      install_requires=[
          'requests==2.25.1',
          'PyYAML==5.3.1',
          'click==7.1.2'
      ],
      entry_points='''
        [console_scripts]
        download=agoda.cli.download:file_downloader
    ''',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      keywords='download',
      author='Diep Dao',
      author_email='diepdaocs@gmail.com',
      license='MIT')
