#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""cbexplorer main module CLI
"""

import click
import jinja2
import os
import yaml

from .zml_parser import Schema

ZML_VERSION = "1.0.0"


def check_zml_version(input_file: str):
    """Checks the ZML version of YAML File being process.
    Prints program ZML version and YAML File version.

    Args:
        input_file (str): ZML YAML File path.

    Returns:
        boolean: return True on ZML version match.
    """
    version = None
    with open(input_file, "r") as f:
        version = f.readline().strip()
    if ZML_VERSION in version:
        return True
    print("Version mismatch zml: " + ZML_VERSION)
    print("YAML file " + version)
    return False


@click.command()
@click.argument("input_file", metavar="[INPUT]", type=click.Path(), required=True)
@click.argument(
    "output_dir", metavar="[OUTPUT_DIRECTORY]", type=click.Path(), required=False
)
def cli(input_file, output_dir):
    if not check_zml_version(input_file):
        return

    plxmap_dict = None
    with open(input_file, "r") as f:
        plxmap_dict = yaml.safe_load(f)

    cb_schemas = []
    for k, v in plxmap_dict.get("components").get("schemas").items():
        if k != "constant":
            cb_schemas.append(Schema(k, v))

    for schema in cb_schemas:
        template_loader = jinja2.FileSystemLoader(searchpath="cbexplorer")
        env = jinja2.Environment(loader=template_loader)
        python_cb = env.get_template("python.jinja").render(cb=schema)

        with open(os.path.join(output_dir, schema.name + ".py"), "w") as f:
            f.write(python_cb)


if __name__ == "__main__":
    cli(prog_name="cbexplorer")
