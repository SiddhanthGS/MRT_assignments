from setuptools import find_packages, setup

package_name = 'siddhanth_s_assn_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='siddy',
    maintainer_email='siddy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "d_rover1 = siddhanth_s_assn_2.d_rover1:main",
            "d_rover2 = siddhanth_s_assn_2.d_rover2:main",
            "d_rover3 = siddhanth_s_assn_2.d_rover3:main",
            "basestation = siddhanth_s_assn_2.basestation:main"
        ],
    },
)
