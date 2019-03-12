import abc


class RefDataInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def test_connection(self):
        raise NotImplementedError('Need to define testConnection method to use this base class.')

    @abc.abstractmethod
    def download(self):
        raise NotImplementedError('Need to define download method to use this base class.')

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError('Need to define update method to use this base class.')

    @abc.abstractmethod
    def backup(self):
        raise NotImplementedError('Need to define update method to use this base class.')

    @abc.abstractmethod
    def restore(self):
        raise NotImplementedError('Need to define update method to use this base class.')

