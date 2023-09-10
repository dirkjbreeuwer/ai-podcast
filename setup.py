from setuptools import setup, find_packages

setup(
    name='ai_podcast',  # Name of your package
    version='0.1',  # Version number
    packages=find_packages(),  # Automatically discover and include all packages in the package directory
    install_requires=[
        # List your project's dependencies here, e.g.,
        # 'numpy',
        # 'pandas',
        'apify-client',
    ],
    entry_points={
        # If you have any scripts or command-line interfaces, define them here
        # 'console_scripts': [
        #     'my_script = my_module:main_function',
        # ],
    },
    # Additional metadata
    author='Dirk Breeuwer',
    description='An AI-powered podcast tool',
    license='MIT',
    keywords='AI podcast',
    url='https://github.com/dirkjbreeuwer/ai-podcast',  # Replace with your repo URL
)
