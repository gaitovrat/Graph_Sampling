from setuptools import setup, find_packages

setup(
    name="graph-sampling",
    version="0.0.2",
    description="Graph Sampling Package",
    long_description="Graph Sampling Package",
    long_description_content_type="text/txt",
    author="Kirti Jain, Ashish Aggarwal",
    author_email="kirtij.mcs16.du@gmail.com, ashish.mcs16.du@gmail.com",
    license="MIT",
    packages=find_packages(),  # Automatically find your Python packages
    python_requires=">=3.10",
    install_requires=["networkx>=3.4.2", "numpy>=2.1.3"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
