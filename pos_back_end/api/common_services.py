from pydantic import BaseModel, ConfigDict


class CommonServices:

    @staticmethod
    def to_camel_case(parameter: str) -> str:
        parts = parameter.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])


class CommonBaseModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=CommonServices.to_camel_case,
        populate_by_name=True
    )