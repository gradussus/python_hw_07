from setuptools import setup

setup(name='clean_folder',
      version='0.0.1',
      description='Sorted folder by extensions',
      url='https://github.com/gradussus/python_hw_06',
      author='Vitalii Shevchenko',
      author_email='test@mail.com',
      license='MIT',
      packages=['clean_folder'], 
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:start']})
