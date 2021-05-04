#!/usr/bin/env python3

import os
import tempfile

from testsupport import run, subtest, warn, test_root, run_project_executable, ensure_library


def main() -> None:
    # Run the test program
    lib = ensure_library("liblockhashmap.so")
    extra_env={"LD_LIBRARY_PATH": str(os.path.dirname(lib))}
    test_lock_hashmap = test_root().joinpath("lock_hashmap")
    times = []
    with tempfile.TemporaryDirectory() as tmpdir:
        with subtest("Checking correctness"):
             with open(f"{tmpdir}/stderr", "w+") as stderr, open(
                    f"{tmpdir}/stdout", "w+"
                ) as stdout:
                run_project_executable(
                        str(test_lock_hashmap),
                        args=["-d20000", "-i10000", "-n4", "-r10000", "-u100", "-b1"],
                        stderr=stderr,
                        stdout=stdout,
                        extra_env=extra_env
                        )
                if os.stat(f"{tmpdir}/stderr").st_size > 0:
                    warn("Test failed with error")
                    exit(1)
        with subtest("Checking 1 thread time"):
             with open(f"{tmpdir}/stderr", "w+") as stderr, open(
                    f"{tmpdir}/stdout", "w+"
                ) as stdout:
                run_project_executable(
                        str(test_lock_hashmap),
                        args=["-d2000000", "-i100000", "-n1", "-r100000", "-u10"],
                        stderr=stderr,
                        stdout=stdout,
                        extra_env=extra_env
                        )
                if os.stat(f"{tmpdir}/stdout").st_size > 0:
                    times.append(float(open(f"{tmpdir}/stdout").readlines()[0].strip()))
                if os.stat(f"{tmpdir}/stderr").st_size > 0:
                    warn("Test failed with error")
                    exit(1)
        with subtest("Checking 2 thread time"):
             with open(f"{tmpdir}/stderr", "w+") as stderr, open(
                    f"{tmpdir}/stdout", "w+"
                ) as stdout:
                run_project_executable(
                        str(test_lock_hashmap),
                        args=["-d2000000", "-i100000", "-n2", "-r100000", "-u10"],
                        stderr=stderr,
                        stdout=stdout,
                        extra_env=extra_env
                        )
                if os.stat(f"{tmpdir}/stdout").st_size > 0:
                    times.append(float(open(f"{tmpdir}/stdout").readlines()[0].strip()))
                if os.stat(f"{tmpdir}/stderr").st_size > 0:
                    warn("Test failed with error")
                    exit(1)
        with subtest("Checking 4 thread time"):
             with open(f"{tmpdir}/stderr", "w+") as stderr, open(
                    f"{tmpdir}/stdout", "w+"
                ) as stdout:
                run_project_executable(
                        str(test_lock_hashmap),
                        args=["-d2000000", "-i100000", "-n4", "-r100000", "-u10"],
                        stderr=stderr,
                        stdout=stdout,
                        extra_env=extra_env
                        )
                if os.stat(f"{tmpdir}/stdout").st_size > 0:
                    times.append(float(open(f"{tmpdir}/stdout").readlines()[0].strip()))
                if os.stat(f"{tmpdir}/stderr").st_size > 0:
                    warn("Test failed with error")
                    exit(1)
    f1 = times[0] / times[1]
    f2 = times[1] / times[2]
    if (f1 < 1.5 or  f1 > 2 or f2 < 1.5 or f2 > 2):
        warn("Hashmap is not scaling properly: " + str(times))
        exit(1)

if __name__ == "__main__":
    main()
