import logging

PLUGIN_PARAMS = {"required": ["first", "last"], "optional": ["middle_name"]}


def demo(params: dict) -> dict:
    """
    Example function formatted for use as a plugin with the dewberry/process-api

    params: Input dictionary with keys listed in PLUGIN_PARAMS["required"]
             (and additional keys listed in PLUGIN_PARAMS["optional"])

    results: OGC Compliant output returned as a dictionary.

    example: main({"first": "foo", "last": "bar", "middle": "who"})
    """
    first, last = params["first"], params["last"]
    logging.info(f"running `my_module.demo` with inputs {params}")

    if params.get("middle") is not None:
        middle = params["middle"]
        results = {"user": f"{first} {middle} {last}"}
    else:
        results = {"user": f"{first} {last}"}

    return results
