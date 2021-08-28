from .signals import product_viewed_signal


class ProductViewedMixin:
    def dispatch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except self.model.DoesNotExist:
            instance = None
        if instance is not None:
            product_viewed_signal.send(
                instance.__class__, instance=instance, request=request)

        return super(
            ProductViewedMixin. self).dispatch(request, *args, **kwargs)
