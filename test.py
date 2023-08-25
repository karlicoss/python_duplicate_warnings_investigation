#!/usr/bin/env python3
import warnings


# each of these lines produces a warnings
warnings.warn("warning1")
warnings.warn("warning1")
warnings.warn("warning1")


for x in range(10):
    # when in loop, it only logs once
    warnings.warn("warning_loop")



def recurse(count):
    if count == 0:
        return
    # this also logs once, as expected?
    warnings.warn("warning_recursive")
    recurse(count - 1)


recurse(count=5)
recurse(count=6)
