from distutils.core import setup

setup(name='sample_package',
      version='0.2',
      description='A description of this project',
      author='Me',
      author_email='test@test.net',
      # Use `packages` argument to tell distutils where the python modules are located.
      # See https://docs.python.org/3/distutils/setupscript.html#listing-whole-packages for more details.
      packages=['sample_package'],
      # Use `install_requires` to specify the dependencies which are required in order to run the package.
      # See https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/ for a differentiation
      # to the `requirements.txt`.
      install_requires=[
            "numpy"
      ]
     )