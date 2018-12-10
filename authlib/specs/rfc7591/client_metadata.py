# https://tools.ietf.org/html/rfc7591#section-2


class ClientMetadata(dict):
    def validate(self):
        pass


def get_response_type(grant_type):
    """Parse "response_type" from the given grant_type via `Section 2.1`_.

    .. _`Section 2.1`: https://tools.ietf.org/html/rfc7591#section-2.1
    """
    if grant_type == 'authorization_code':
        return 'code'
    if grant_type == 'implicit':
        return 'token'
    return None
