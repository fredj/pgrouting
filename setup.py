from setuptools import setup, find_packages

version = '0.0'

setup(name = 'pgrouting',
      version = version,
      description = "routing with pgRouting tools, OpenStreetMap road data and GeoExt.",
      long_description = "",
      author = 'Daniel Kastl, Frederic Junod',
      packages = find_packages(),
      include_package_data = True,
      zip_safe = False,
      install_requires = ["Flask", "SQLAlchemy", "psycopg2"]
)
