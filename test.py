#!/usr/bin/env python3
import warnings

# each of these lines produces a warning
# since each line considered as a diferent warning context
warnings.warn("warning")
warnings.warn("warning")
warnings.warn("warning")


for x in range(10):
    # when in loop, it only logs once (since it only cares about the line number)
    warnings.warn("warning_loop")


# the way this works is python keeping track of the warning registry
# the registry caches filename, line number and warning category
# https://github.com/python/cpython/blob/ea77520094085ff86160f64fd4bc4f7e8e4ec0d2/Lib/warnings.py#L346


def recurse(count=5):
    if count == 0:
        return
    # this also prints warning only once
    warnings.warn("warning_recursive")
    recurse(count - 1)


# this will print the warning
recurse()
# this won't
recurse()


# HOWEVER, python also keeps track of the 'filter version'
# so when these filters change, python resets the registry completely
# https://github.com/python/cpython/blob/ea77520094085ff86160f64fd4bc4f7e8e4ec0d2/Lib/warnings.py#L337

# for example, this will reset the registry
with warnings.catch_warnings():
    pass

# so the first call here will print warning again
recurse()
# a repeated call after that won't result in warning
recurse()


# sadly subprocess uses catch_warnings internally
# see https://github.com/python/cpython/issues/73858#issuecomment-1692635121
import subprocess
subprocess.check_call(['echo'])

# so this will print the warning again.. ugh
recurse()


