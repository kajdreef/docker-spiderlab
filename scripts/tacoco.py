"""
Script for running tacoco on a project
"""
#!/bin/python3
import argparse
import subprocess
import os


def parse_arguments():
    """
    Parse arguments to run Tacoco
    """
    parser = argparse.ArgumentParser(description='Run Tacoco')

    parser.add_argument('sut', type=str,
                        help="Absolute path to system-under-test's root.")

    parser.add_argument('--out', type=str, help="absolute path to output directory")

    return parser.parse_args()


if __name__ == "__main__":
    os.chdir("/usr/spiderlab/tools/tacoco/")
    ARGS = parse_arguments()

    SUT = ARGS.sut

    if not os.path.isdir(SUT):
        print("SUT path is not a directory...")
        exit(-1)

    OUT = "/usr/spiderlab/output/{}/".format((SUT.split("/"))[-2])

    if ARGS.out is not None:
        OUT = ARGS.out

    CMD = [
        "mvn",
        "-q",
        "exec:java",
        "-Plauncher",
        "-Dtacoco.sut={}".format(SUT),
        "-Dtacoco.outdir={}".format(OUT),
        "-Danalyzer.opts=/usr/spiderlab/tools/blinky/blinky-tacoco/src/main/resources/blinky-analyzer.config",
        "-Dtacoco.log"
    ]

    subprocess.call(CMD)
