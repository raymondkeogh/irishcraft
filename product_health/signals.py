from django.dispatch import Signal

product_viewed_signal = Signal(providing_args=['instance', 'request'])