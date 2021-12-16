#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ZML OpenAPI Parser
"""


def flatten_properties(key: str, values: dict, parent_offset):
    field_offset = parent_offset
    if "x-zml-offset" in values:
        field_offset += values["x-zml-offset"]
    elif "x-zml-bit-offset" in values:
        field_offset += values["x-zml-bit-offset"]
    field_type = values.get("type")
    field_format = values.get("format")
    field_description = values.get("description")
    field_size = values.get("x-zml-size")
    field_properties = values.get("properties")
    field_min_items = values.get("minItems")
    field_max_items = values.get("maxItems")
    field_output = {
        "name": key,
        "type": field_type,
        "description": field_description,
        "format": field_format,
        "minItems": field_min_items,
        "maxItems": field_max_items,
        "offset": field_offset,
        "size": field_size,
        "items": [],
    }

    if field_type != "array":
        yield field_output

    if field_type == "object":
        for k, v in field_properties.items():
            yield from flatten_properties(k, v, field_offset)
    elif field_type == "array":
        for field in flatten_properties(
            key + "__@0", values.get("items"), field_offset
        ):
            field_output["items"].append(field)
        yield field_output


class Schema:
    def __init__(self, key: str, properties: dict):
        self.name = key
        self.description = properties.get("description")
        self.offset = properties.get("x-zml-offset")
        self.properties = []

        for k, v in properties.get("properties").items():
            for field in flatten_properties(k, v, self.offset):
                self.properties.append(field)
