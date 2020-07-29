import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

### Apps Definition ###
app_package = 'historical_validation_tool_dominican_republic'
release_package = 'tethysapp-' + app_package
app_class = 'historical_validation_tool_dominican_republic.app:HistoricalValidationToolDominicanRepublic'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

### Python Dependencies ###
dependencies = [
    'pandas',
    'requests',
    'plotly',
    'numpy',
    'datetime',
    'hydrostats',
    'scipy',
    'xmltodict',
    'requests',
]

setup(
    name=release_package,
    version='0.0.1',
    tags='',
    description='This app evaluates the accuracy for the historical streamflow values obtained from Streamflow Prediction Tool in Dominican Republic.',
    long_description='',
    keywords='Historical Validation Tool',
    author='Jorge Luis Sanchez-Lozano',
    author_email='jorgessanchez7@gmail.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)
