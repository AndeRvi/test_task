from django.views.generic import TemplateView


class ErrorView(TemplateView):
    template_name = 'error.html'

    def get_context_data(self, error=None, **kwargs):

        if error:
            kwargs.update({
                'error': error,
            })

        return super(ErrorView, self).get_context_data(**kwargs)
