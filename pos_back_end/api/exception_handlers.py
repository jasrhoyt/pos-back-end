from fastapi import Request
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse


def format_field_name(field_name: str) -> str:
    """Replace underscores with spaces and capitalize each word."""
    return field_name.replace("_", " ").title()


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    print("Validation errors:", errors)  # Debug log
    missing_fields = []

    for error in errors:
        # Handle both 'missing' and 'string_type' errors with None input
        if error["type"] == "missing" or (
            error["type"] == "string_type" and error["input"] is None
        ):
            loc = error["loc"]
            field_name = loc[-1]  # Get the last part of the location path
            # Format the final field name, ignoring parent fields
            formatted_name = format_field_name(field_name)
            missing_fields.append(formatted_name)

    error_message = f"The following field(s) are missing: {', '.join(missing_fields)}"

    return JSONResponse(
        status_code=422,
        content={
            "statusCode": 422,
            "errorMessage": error_message,
        }
    )


async def conflict_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 409:
        error_message = exc.detail or "Resource conflict occurred"
        print(f"Conflict error: {error_message}")  # Debug log

        return JSONResponse(
            status_code=409,
            content={
                "statusCode": 409,
                "errorMessage": error_message,
            }
        )
    raise exc
