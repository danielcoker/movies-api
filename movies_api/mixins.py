class SuccessMessageMixin:
    """
    Adds a resource name and success message to the renderer context to be used by
    a custom renderer to display success messages.
    """
    resource_name = None
    success_message = None

    def get_renderer_context(self):
        context = super().get_renderer_context()

        try:
            context['resource_name'] = type(self.get_queryset()[0]).__name__ if hasattr(
                self, 'get_queryset') else self.resource_name
        except IndexError as e:
            context['success_message'] = self.success_message = 'No records found.'

        context['success_message'] = self.success_message

        return context
