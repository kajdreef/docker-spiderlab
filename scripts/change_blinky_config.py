"""
Script for configuring blinky with tacoco (i.e., at what level will we instrument the program.)
"""
#!/bin/python3
import argparse


def parse_arguments():
    """
    Parse arguments for the blinky configuration
    """
    parser = argparse.ArgumentParser(description='Change blinky run configurations.')

    parser.add_argument('blinky_opts', type=str,
                        help="Blinky options to configure what is going to be instrumented.")

    return parser.parse_args()

if __name__ == "__main__":
    print("Change Blinky run configuration.")
    ARGS = parse_arguments()

    BLINKY_CONFIG = "\
    -javaagent:/usr/spiderlab/tools/blinky/blinky-core/target/blinky-core-0.0.1-SNAPSHOT-jar-with-dependencies.jar={}\n\
    -cp:/usr/spiderlab/tools/blinky/blinky-tacoco/target/blinky-tacoco-0.0.1-SNAPSHOT-jar-with-dependencies.jar\n\
    -Dtacoco.listeners=org.spideruci.analysis.tacoco.BlinkyListener \n\
    -Dtacoco.analyzer=org.spideruci.analysis.tacoco.BlinkyAnalyzer \
    ".format(ARGS.blinky_opts)

    with open("/usr/spiderlab/tools/blinky/blinky-tacoco/src/main/resources/blinky-analyzer.config", 'w') as f:
        f.write(BLINKY_CONFIG)
