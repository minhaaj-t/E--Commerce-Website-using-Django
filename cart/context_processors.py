from .models import Cart,Cart_items
from .views import _cart_id_

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id_(request))
            cart_item=Cart_items.objects.all().filter(cart=cart[:1])
            for cart_item in cart_item:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)

