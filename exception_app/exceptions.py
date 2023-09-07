class ObjectNotFoundException(Exception):
    def __init__(self, object_name, message="Object you are trying to access does not exist"):
        self.object_name = object_name
        self.message = message
        super().__init__(self.message)

class InvalidDataException(Exception):
    def __init__(self, message="Only new orders can be dispatched"):
        # import pdb;pdb.set_trace()
        self.message = message
        super().__init__(self.message)

class ServiceException(Exception):
    def __init__(self, message="Service exception"):
        self.message = message
        super().__init__(self.message)
