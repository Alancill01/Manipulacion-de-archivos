import json
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct
json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    object_hook=as_complex)
(1+2j)
import decimal
json.loads('1.1', parse_float=decimal.Decimal)
