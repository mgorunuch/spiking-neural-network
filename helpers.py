import time
import math


def attach_to_dict_by_key(array, key, value, offset=0):
    keys = key.split(".")

    if keys[offset] not in array:
        array[keys[offset]] = {}

    if len(keys) > offset + 1:
        attach_to_dict_by_key(array[keys[offset]], key, value, offset + 1)
        return

    array[keys[offset]] = value


def detach_from_dict_by_key(array, key, offset=0):
    keys = key.split(".")

    if keys[offset] not in array:
        return

    if len(keys) > offset + 1:
        detach_from_dict_by_key(array[keys[offset]], key, offset + 1)
        return

    del array[keys[offset]]


def get_from_dict_by_key(array, key, default_value, offset=0):
    keys = key.split(".")

    if keys[offset] not in array:
        return default_value

    if len(keys) == offset + 1:
        return array[keys[offset]]

    return get_from_dict_by_key(array[keys[offset]], key, default_value, offset + 1)


def current_milliseconds_time():
    return int(round(time.time() * 1000))


def dict_items_in_range(dictionary, from_key, to_key):
    result_keys = list(
        filter(
            lambda a: from_key < int(a) < to_key,
            dictionary.keys()
        )
    )

    values = []
    for i in range(len(result_keys)):
        values.append(
            dictionary[str(result_keys[i])]
        )

    return values


def distance(p1, p2):
    """
    Дистанция между двумя точками в пространстве
    """
    return math.sqrt(
        (p1[0] - p2[0])**2 +
        (p1[1] - p2[1])**2 +
        (p1[2] - p2[2])**2
    )


def multiplier_increment(p1, p2, nm):
    return (
        math.ceil((p2[0] - p1[0]) / nm),
        math.ceil((p2[1] - p1[1]) / nm),
        math.ceil((p2[2] - p1[2]) / nm),
    )
