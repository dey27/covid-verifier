import logging

def response_dict(data=None, msg="", stats={}, code=200, print_full_logs=True):
    """
    Usage - return JsonResponse(response_dict(data={}, code=200, print_full_logs=False))
    """
    response = {
        "meta": {
            "code": code,
            "message": msg,
            "data_statistics": stats
        },
        "data": data,
    }

    if print_full_logs:
        logging.info("{}-{}".format(response['meta'], response['data']))

    return response
