#!/bin/python3
import argparse
import subprocess
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description='Run Tacoco')

    parser.add_argument('sut', type=str,
                        help="Absolute path to system-under-test's root.")
    
    return parser.parse_args()


if __name__ == "__main__":
    os.chdir("/usr/spiderlab/tools/tacoco/")
    args = parse_arguments()

    sut = args.sut

    if not os.path.isdir(sut):
        print("SUT path is not a directory...")
        exit(-1)
    
    outdir = "/usr/spiderlab/output/{}/".format((sut.split("/"))[-2])
    
    cmd = [
        "mvn",
        "-q",
        "exec:java",
        "-Plauncher",
        "-Dtacoco.sut={}".format(sut),
        "-Dtacoco.outdir={}".format(outdir),
        "-Danalyzer.opts=/usr/spiderlab/tools/blinky/blinky-tacoco/src/main/resources/blinky-analyzer.config",
        "-Dtacoco.log"
    ]

    subprocess.call(cmd)
