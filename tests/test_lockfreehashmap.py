#!/usr/bin/env python3

import os
import tempfile

from testsupport import run, subtest, warn, test_root, run_project_executable, ensure_library


def main() -> None:
    # Run the test program
    test_lock_hashmap = test_root().joinpath("lockfree_hashmap")
    if not test_lock_hashmap.exists():
        run(["make", "-C", str(test_root()), str(test_lock_hashmap)])
    times = []
    with tempfile.TemporaryDirectory() as tmpdir:
        with subtest("Checking correctness"):
            with open(f"{tmpdir}/stdout", "w+") as stdout:
                run_project_executable(
                        str(test_lock_hashmap),
                        args=["-d20000", "-i10000", "-n4", "-r10000", "-u100", "-b1"],
                        stdout=stdout)
        with subtest("Checking 1 thread time"):
            with open(f"{tmpdir}/stdout", "w+") as stdout:
                run_project_executable(
                        str(test_lock_hashmap),
                        args=["-d20000", "-i10000", "-n1", "-r10000", "-u10", "-b1"],
                        stdout=stdout)
                times.append(float(open(f"{tmpdir}/stdout").readlines()[0].strip()))
        with subtest("Checking 2 thread time"):
            with open(f"{tmpdir}/stdout", "w+") as stdout:
                run_project_executable(
                        str(test_lock_hashmap),
                        args=["-d20000", "-i10000", "-n2", "-r10000", "-u10", "-b1"],
                        stdout=stdout)
                times.append(float(open(f"{tmpdir}/stdout").readlines()[0].strip()))
        with subtest("Checking 4 thread time"):
            with open(f"{tmpdir}/stdout", "w+") as stdout:
                run_project_executable(
                        str(test_lock_hashmap),
                        args=["-d20000", "-i10000", "-n4", "-r10000", "-u10", "-b1"],
                        stdout=stdout
                        )
                times.append(float(open(f"{tmpdir}/stdout").readlines()[0].strip()))
    f1 = times[0] / times[1]
    f2 = times[1] / times[2]
    if (f1 < 1.4 or  f1 > 2.2 or f2 < 1.4 or f2 > 2.2):
        warn("Hashmap is not scaling properly: " + str(times))
        exit(1)

if __name__ == "__main__":
    main()
