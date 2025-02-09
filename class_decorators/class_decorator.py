import functools

def invariant(predicate):

    def invariant_checking_class_decorator(cls):

        method_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_with_invariant_checking_proxy(cls, name, predicate)
        return cls
    return invariant_checking_class_decorator

def _wrap_method_with_invariant_checking_proxy(cls, name, predicate):
    method = getattr(cls, name)
    assert callable(method)

    @functools.wraps(method)
    def invariant_checking_method_decorator(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not predicate(self):
            raise RuntimeError(f'Class invariant {predicate.__doc__} violated for {self}')
        return result
    setattr(cls, name, invariant_checking_method_decorator)
def not_below_absolute_zero(temprature):
    """Temprature not below abolute zero"""
    return temprature._kelvin >= 0


@invariant(not_below_absolute_zero)
class Temprature:

    def __init__(self, kelvin):
        self._kelvin = kelvin

    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, value):
        self._kelvin = value

t = Temprature(5.0)

t1 = Temprature(-5.0)
