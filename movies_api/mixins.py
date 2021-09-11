from rest_framework import views


class SuccessMessageMixin(views.APIView):
    success_message = None

    def get_renderer_context(self):
        context = super().get_renderer_context()
        context['success_message'] = self.success_message

        return context
