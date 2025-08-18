from setuptools import setup, find_packages

setup(
    name="django-library-management",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Django>=4.2",
        "djangorestframework",
        "djongo",
        "gunicorn",
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "manage=manage:main",
        ],
    },
)
