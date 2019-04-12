"""
Script for running blinky on a project
"""
#!/bin/python3
import argparse
import subprocess

def parse_arguments():
    """
    Parse arguments to run blinky
    """
    parser = argparse.ArgumentParser(description='Run Blinky')

    parser.add_argument('blinky_args', type=str,
        help="Profiler configurations, to control the kind of traces that are generated")

    parser.add_argument('mainClass', type=str, help="Main class of the system under analysis.")

    return parser.parse_args()

if __name__ == "__main__":
    ARGS = parse_arguments()

    BLINKY_CONFIG = ARGS.blinky_args
    MAIN_CLASS = ARGS.mainClass

    BLINKY_JAR = "/usr/spiderlab/tools/blinky/blinky-core/target/blinky-core-0.0.1-SNAPSHOT-jar-with-dependencies.jar"

    CMD = [
        "java",
        "-Xbootclasspath/p:{}".format(BLINKY_JAR),
        "-javaagent:{}:{}".format(BLINKY_JAR, BLINKY_CONFIG),
        MAIN_CLASS
    ]

    subprocess.call(CMD)
