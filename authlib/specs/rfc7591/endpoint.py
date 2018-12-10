from .client_metadata import ClientMetadata


class ClientRegistrationEndpoint(object):
    REQUEST_CONTENT_TYPE = 'application/json'
    #: customize client_metadata_cls
    client_metadata_cls = ClientMetadata

    def __init__(self):
        pass

    def validate_endpoint_request(self):
        pass

    def create_endpoint_response(self):
        pass
