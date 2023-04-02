from setuptools import setup, find_packages

setup(
    name='inception',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'chardet',
        'getch',
        'pydeps',
        'pipdeptree',
    ],
    entry_points={
        'console_scripts': [
            'inception-send-files=inception.introspect.send_files.send_files:send_files',
            'inception-function-sigs=inception.introspect.function_signatures.function_sigs:process_directory_recursively'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

