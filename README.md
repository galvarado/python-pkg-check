# python-pkg-check
Unit test to check if Python has all required packages.

## How t use it

Place your dependencies file in the requirements.txt file. You can obtaint it using pip:

```
$ pip list --format=freeze
```


To execute the tests, execute it as follows (inside the test directory):

```

$ python3 -m unittest check_pkg
```

If the test finds out a missing package, you will see it as follows:
```

======================================================================
ERROR: test_requirements (check_pkg.TestRequirements) (requirement='pandas')
Test that each required package is available.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/guillermo/Projects/python-pkg-check/tests/check_pkg.py", line 21, in test_requirements
    pkg_resources.require(requirement)
  File "/usr/lib/python3.7/site-packages/pkg_resources/__init__.py", line 900, in require
    needed = self.resolve(parse_requirements(requirements))
  File "/usr/lib/python3.7/site-packages/pkg_resources/__init__.py", line 786, in resolve
    raise DistributionNotFound(req, requirers)
pkg_resources.DistributionNotFound: The 'pandas' distribution was not found and is required by the application

----------------------------------------------------------------------
Ran 1 test in 0.061s

FAILED (errors=1)
```


If all the dependencies are ok, you will the following result:

```

----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```


## Dependencies

To use this unittest, pathlib must be installed:

```
$ pip install pathlib
```

More info at: https://docs.python.org/3/library/pathlib.html