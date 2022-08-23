from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='UKpostcodes1',
  version='0.0.1',
  description='this library validates the formatting of UK post codes',
  long_description='This library validates the formatting of UK post codes. Also gives the Inward and Outward codes. This library can also fetch address of a post code.',
  url='',  
  author='Sumit Patil',
  author_email='sumitpatil.0704@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Post code', 
  packages=find_packages(),
  install_requires=['geopy==2.2.0','requests==2.28.1'] 
)