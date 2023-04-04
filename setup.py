from setuptools import setup, find_packages

setup(
    name='inception',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'chardet',
        'getch',
        'pydeps',
        'pipdeptree',
        'pyperclip',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'isend = inception.introspect.send_files.send_files:main',
            'ibootstrap = inception.introspect.send_files.whole_project:send_whole_project',
            'idecode = inception.decode.content_block:prompt_and_decode_content_block',
            'inception-function-sigs = inception.introspect.functions.function_sigs:process_directory_recursively [root_directory]'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
