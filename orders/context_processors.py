from .models import ProductInBusket
def getting_busket_info(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	products_in_busket = ProductInBusket.objects.filter(session_key=session_key, is_active=True)
	product_total_number = products_in_busket.count()
	return locals()