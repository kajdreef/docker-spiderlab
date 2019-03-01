#!/bin/python3
import argparse
import subprocess

def parse_arguments():
    parser = argparse.ArgumentParser(description='Run Blinky')

    parser.add_argument('blinky_args', type=str,  help="Profiler configurations, to control the kind of traces that are generated")
    parser.add_argument('mainClass', type=str, help="Main class of the system under analysis.")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    blinky_args = args.blinky_args
    main_class = args.mainClass

    blinky_core_jar = "/usr/spiderlab/tools/blinky/blinky-core/target/blinky-core-0.0.1-SNAPSHOT-jar-with-dependencies.jar"
    
    cmd = [
        "java",
        "-Xbootclasspath/p:{}".format(blinky_core_jar),
        "-javaagent:{}:{}".format(blinky_core_jar, blinky_args),
        main_class
    ]

    subprocess.call(cmd)
