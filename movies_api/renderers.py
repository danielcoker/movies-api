from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status = renderer_context.get('response').status_code
        success_message = renderer_context.get('success_message')
        message = data.get('detail', success_message)
        detail_in_data = 'detail' in data
        errors = None

        # If data contains "detail" field, it means the request failed and the an
        # error response message is available.
        # This error message should be returned only in the "message" field.
        if detail_in_data:
            data = None

        # If data does not contain "detail" field and the status code is 400,
        # it means there is a Validation Error.
        if not detail_in_data and status == 400:
            errors = data
            message = 'Invalid input data.'
            data = None

        # Construct the response data structure.
        raw_response_data = {'success': status < 400, 'message': message, 'errors': errors,
                             'data': data, }

        # Remove response data items that have None value.
        response_data = {k: v for k,
                         v in raw_response_data.items() if v is not None}

        response = super(CustomJSONRenderer, self).render(
            response_data, accepted_media_type, renderer_context)

        return response
