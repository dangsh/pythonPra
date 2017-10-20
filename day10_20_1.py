from abc import ABCMeta , abstractmethod
class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        assert False , "zijishixian"

class Sub(Super):
    def action(self):
        print("zijishixinale   le")

x = Sub()
x.delegate()