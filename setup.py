from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="domain-gistry",
    version="1.0.0",
    description="A Domain Name Generation CLI.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jcharis/DomainGistry_CLI",
    author="Jesse E.Agbe(JCharis)",
    author_email="jcharistech@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["domain-gistry"],
    include_package_data=True,
    install_requires=["click","click-didyoumean"],
    entry_points={
        "console_scripts": [
            "domain-gistry=domain-gistry.domain-gistry:main",
        ]
    },
)
