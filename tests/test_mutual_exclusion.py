#!/usr/bin/env python3

import os
import tempfile

from testsupport import run, subtest, warn, test_root, run_project_executable, ensure_library


def main() -> None:
    # Run the test program
    lib = ensure_library("libcspinlock.so")
    extra_env={"LD_LIBRARY_PATH": str(os.path.dirname(lib))}
    test_mutual_exclusion = test_root().joinpath("test_mutual_exclusion")
    if not test_mutual_exclusion.exists():
        run(["make", "-C", str(test_root()), str(test_mutual_exclusion)])
    with tempfile.TemporaryDirectory() as tmpdir:
        with subtest("Checking mutual exclusion"):
             with open(f"{tmpdir}/stderr", "w+") as stderr, open(
                    f"{tmpdir}/stdout", "w+"
                ) as stdout:
                run_project_executable(
                        str(test_mutual_exclusion),
                        stderr=stderr,
                        stdout=stdout,
                        extra_env=extra_env
                        )
                if os.stat(f"{tmpdir}/stdout").st_size > 0:
                    warn("Test did not pass")
                    exit(1)
                if os.stat(f"{tmpdir}/stderr").st_size > 0:
                    warn("Test failed with error")
                    exit(1)

if __name__ == "__main__":
    main()
