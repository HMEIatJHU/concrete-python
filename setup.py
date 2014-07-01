from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

setup(
    name = "concrete",
    version = "3.0.2pre",
    packages = [
        'concrete',

        # Python code generated by Thrift Compiler
        'concrete.audio',
        'concrete.communication',
        'concrete.communication_service',
        'concrete.discourse',
        'concrete.email',
        'concrete.entities',
        'concrete.language',
        'concrete.metadata',
        'concrete.situations',
        'concrete.spans',
        'concrete.structure',
        'concrete.twitter',

        # Python code generated by people
        'concrete.util',
        'tests',
        ],

    scripts = [
        'scripts/concrete2json.py',
        'scripts/validate_communication.py',
        ],

    test_suite = "tests",

    install_requires = [
        'networkx',
        'testfixtures',
        'thrift>=0.9.1',
        ],

    url = "https://github.com/hltcoe/concrete-python",
    license="BSD",
)
