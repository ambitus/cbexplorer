#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

import json
import yaml
from enum import Enum
from collections import OrderedDict


def yaml_ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
    )

    return yaml.load(stream, OrderedLoader)


class LoaderType(Enum):
    JSON = 1
    YAML = 2


class Loader:
    @staticmethod
    def load(file_path, file_type=LoaderType.YAML):
        switcher = {
            LoaderType.JSON: lambda x: json.load(x, object_pairs_hook=OrderedDict),
            LoaderType.YAML: lambda x: yaml_ordered_load(x),
        }

        func = switcher.get(file_type)
        with open(file_path, "r") as f:
            return func(f)
