from setuptools import setup, find_packages

version = '0.0'

setup(name='pgrouting',
      version=version,
      description="routing with pgRouting tools, OpenStreetMap road data and GeoExt.",
      long_description="",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='pgRouting OpenStreetMap',
      author='',
      author_email='',
      url='http://2010.foss4g.org/workshop10.php',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
