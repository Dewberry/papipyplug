import sys

from .my_module import PLUGIN_PARAMS, demo
from papipyplug import parse_input, print_results, plugin_logger

if __name__ == "__main__":
    # Start plugin logger
    plugin_logger()

    # Read, parse, and verify input parameters
    input_params = parse_input(sys.argv, PLUGIN_PARAMS)

    # Add main function here
    results = demo(input_params)

    # Print Results
    print_results(results)
