""" 
All the user defined exceptions that can be raised by the page model and app

"""

class PublishError(Exception):
    # logic for publish error
    def __str__(self):
        return f"Can't publish a pending or inactive page. Make sure the status of the page is active and try again."
