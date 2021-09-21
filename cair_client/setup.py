from setuptools import setup

package_name = 'cair_client'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lucrezia Grassi',
    maintainer_email='lucrezia.grassi@edu.unige.it',
    description='Package containing the service that allows to connect to the CAIR cloud.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'service = cair_client.cair_srv:main',
        	'client = cair_client.cair_node:main',
        ],
    },
)
