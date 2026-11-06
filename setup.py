from setuptools import setup, find_packages
setup(
    name="neutron-utils",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy>=1.24", "scipy>=1.10", "mpi4py>=3.1", "h5py>=3.8"],
    python_requires=">=3.10",
    description="Neutron transport calculations for reactor physics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Neutron Physics Group",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
