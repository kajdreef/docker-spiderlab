#!/bin/python3
import argparse
import subprocess
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description='Change blinky run configurations.')

    parser.add_argument('blinky_opts', type=str,
                        help="Blinky options to configure what is going to be instrumented.")

    return parser.parse_args()

if __name__ == "__main__":
    print("Change Blinky run configuration.")
    args = parse_arguments()

    blinky_config = "\
    -javaagent:/usr/spiderlab/tools/blinky/blinky-core/target/blinky-core-0.0.1-SNAPSHOT-jar-with-dependencies.jar={}\n\
    -cp:/usr/spiderlab/tools/blinky/blinky-tacoco/target/blinky-tacoco-0.0.1-SNAPSHOT-jar-with-dependencies.jar\n\
    -Dtacoco.listeners=org.spideruci.analysis.tacoco.BlinkyListener \n\
    -Dtacoco.analyzer=org.spideruci.analysis.tacoco.BlinkyAnalyzer \
    ".format(args.blinky_opts)

    with open("/usr/spiderlab/tools/blinky/blinky-tacoco/src/main/resources/blinky-analyzer.config", 'w') as f:
        f.write(blinky_config)
