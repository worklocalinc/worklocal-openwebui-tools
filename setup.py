from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="worklocal-openwebui-tools",
    version="1.0.0",
    author="WorkLocal Team",
    author_email="dev@worklocal.app",
    description="OpenWebUI tools for WorkLocal infrastructure management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/worklocalinc/worklocal-openwebui-tools",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "pyyaml>=6.0",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=5.0",
            "mypy>=0.990",
        ],
    },
)