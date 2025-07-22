from setuptools import setup, find_packages

setup(
    name="UTUC_Classifier",
    version="0.1.0",
    description="UTUC molecular subtype classifier",
    author="Hoho1996",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tensorflow",
        "keras",
        "numpy",
        "pandas"
    ],
    package_data={"UTUC_Classifier": ["models/*.h5"]},
)