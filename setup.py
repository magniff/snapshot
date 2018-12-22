import setuptools


classifiers = [
    (
        "Programming Language :: Python :: %s" % x
    )
    for x in "3.1 3.2 3.3 3.4 3.5 3.6 3.7".split()
]


setuptools.setup(
    name="snapshot",
    description="Wierd and inefficient Tar clone.",
    version="0.0.1",
    license="MIT license",
    platforms=["unix", "linux", "osx", "win32"],
    author="magniff",
    url="https://github.com/magniff/snapshot",
    classifiers=classifiers,
    install_requires=[
        "sqlalchemy", "watch"
    ],
    packages=setuptools.find_packages(),
    zip_safe=False,
)
