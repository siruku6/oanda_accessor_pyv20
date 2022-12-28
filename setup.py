# Making this file, auther refered to the following repositories.
# - psf / requests
#     https://github.com/psf/requests
#
# - c60evaporator / seaborn-analyzer
#     https://github.com/c60evaporator/seaborn-analyzer
#
#     This is made by the author of this article.
#     - 【PyPI】Pythonの自作ライブラリをpipに公開する方法
#     https://qiita.com/c60evaporator/items/e1ecccab07a607487dcf

from setuptools import setup
import oanda_accessor_pyv20

DESCRIPTION = "This app lets you easily load candle data of Foreign Currency from Oanda API."
NAME = "oanda_accessor_pyv20"
AUTHOR = "siruku6"
AUTHOR_EMAIL = "sirukufarios@gmail.com"
URL = "https://github.com/siruku6/oanda_accessor_pyv20"
LICENSE = "MIT License"
DOWNLOAD_URL = "https://github.com/siruku6/oanda_accessor_pyv20"
VERSION = oanda_accessor_pyv20.__version__
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = [
    "oandapyV20==0.7.2",
    "pandas>=1.0.0, <=1.4.3",
]
EXTRAS_REQUIRE = {
    "dev": [
        # NOTE: necessary to build this package
        "setuptools",
        "twine",
        "wheel",
    ],
}
TEST_REQUIRES = [
    "pytest>=3",
]


PACKAGES = [
    "oanda_accessor_pyv20"
]

CLASSIFIERS = [
    # NOTE: Refer to this link, https://pypi.org/search/
    "Topic :: Office/Business :: Financial :: Investment",
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    tests_require=TEST_REQUIRES,
    packages=PACKAGES,
    classifiers=CLASSIFIERS
)
