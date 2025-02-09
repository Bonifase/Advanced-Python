import functools

def invariant(predicate):

    def invariant_checking_class_decorator(cls):

        method_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_with_invariant_checking_proxy(cls, name, predicate)

        property_names = [name for name, attr in vars(cls).items() if isinstance(attr, property)]
        for name in method_names:
            _wrap_property_with_invariant_checking_proxy(cls, name, predicate)

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

def _wrap_property_with_invariant_checking_proxy(cls, name, predicate):
    prop = getattr(cls, name)
    assert callable(prop)

    invariant_checking_proxy = InvariantCheckingPropertyProxy(prop, predicate)
    setattr(cls, name, invariant_checking_proxy)

class InvariantCheckingPropertyProxy:
    def __init__(self, referent, predicate):
        self._referent = referent
        self._predicate = predicate

    def __get__(self, instance, owner):
        if instance is None:
            return self._referent
        result = self._referent.__get__(instance, owner)
        if not self._predicate(instance):
            raise RuntimeError(f'Class invariant {self._predicate.__doc__} violated for {instance}')
        return result

    def __set__(self, instance, value):
        result = self._referent.__set__(instance, value)
        if not self._predicate(instance):
            raise RuntimeError(f'Class invariant {self._predicate.__doc__} violated for {instance}')
        return result

    def __delete__(self, instance):
        result = self._referent.__delete__(instance)
        if not self._predicate(instance):
            raise RuntimeError(f'Class invariant {self._predicate.__doc__} violated for {instance}')
        return result


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

    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self._kelvin = value + 273.15

    @property
    def fahrenheit(self):
        return self._kelvin * 9/5 - 459.67

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._kelvin = (value + 459.67) * 5/9


t = Temprature(5.0)

t1 = Temprature(-5.0)
