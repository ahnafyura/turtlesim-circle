from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtlesim_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/circle.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ahnaf',
    maintainer_email='ahnafalghiffarriahtasyafi@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'circle_controller = turtlesim_nodes.circle_controller:main',
        ],
    },
)
