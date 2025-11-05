import re
from pint import UnitRegistry
import sys

ureg = UnitRegistry()

def to_second(text):
    try:
        text = text.strip().lower()

        text = re.sub(r'µ', 'u', text)  # reemplazar símbolo µ
        text = text.replace('us', ' microsecond')
        text = text.replace('ms', ' millisecond')
        text = text.replace('ns', ' nanosecond')
        text = text.replace('ps', ' picosecond')
        text = text.replace('mv', ' millivolt')
        text = text.replace('uv', ' microvolt')
        text = text.replace('nv', ' nanovolt')
        text = text.replace('kv', ' kilovolt')

        # asegurar que ' s' y ' v' estén bien definidos
        text = re.sub(r'(\d)\s*s\b', r'\1 second', text)
        text = re.sub(r'(\d)\s*v\b', r'\1 volt', text)

        # Crear cantidad y convertir
        q = ureg.Quantity(text)
        return q.to('second').magnitude
    except (AttributeError, TypeError) as e:
        print(f"Error: no es un string. Objeto={text}, tipo={type(text)}")
        sys.exit(1)
        return None


def to_volt(text):
    text = text.strip().lower()

    # Normalizar micro, mili, etc.
    text = re.sub(r'µ', 'u', text)  # reemplazar símbolo µ
    text = text.replace('us', ' microsecond')
    text = text.replace('ms', ' millisecond')
    text = text.replace('ns', ' nanosecond')
    text = text.replace('ps', ' picosecond')
    text = text.replace('mv', ' millivolt')
    text = text.replace('uv', ' microvolt')
    text = text.replace('nv', ' nanovolt')
    text = text.replace('kv', ' kilovolt')

    # asegurar que ' s' y ' v' estén bien definidos
    text = re.sub(r'(\d)\s*s\b', r'\1 second', text)
    text = re.sub(r'(\d)\s*v\b', r'\1 volt', text)

    # Crear cantidad y convertir
    q = ureg.Quantity(text)
    return q.to('volt').magnitude
