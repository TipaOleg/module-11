import pprint
def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes_and_methods = dir(obj)
    attributes = [item for item in attributes_and_methods if not callable(getattr(obj, item))]
    methods = [item for item in attributes_and_methods if callable(getattr(obj, item))]

    obj_module = getattr(obj, '__module__', None)

    extra_info = {}
    if isinstance(obj, (int, float, str, list, tuple, dict, set)):
        extra_info['length'] = len(obj) if hasattr(obj, '__len__') else 'Not applicable'

    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'extra_info': extra_info
    }

    return result

number_info = introspection_info(42)
pprint.pprint(number_info)