

class CommonServices:

    @staticmethod
    def to_camel_case(parameter: str) -> str:
        parts = parameter.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])