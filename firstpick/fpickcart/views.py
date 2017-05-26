from django.shortcuts import render
from fpickcart.models import Cart
from fpickapp.models import *
# Create your views here.

def add_to_cart(request,modeltype,itemid):
	try:
		logged_in = request.user
		if (modeltype=='laptop') or (modeltype=='desktop'):
			item_price=Computer.objects.get(pk=itemid).price
		cart = Cart(user_id=logged_in,product_id=itemid,price=item_price)
		cart.save()
		context_dict = {'message':'item added successfully'}
	except Exception as e:
		context_dict = {'message':'item not added'}
	return render(request,'cart.html',context_dict)

def view_cart(request):
	cart = Cart.objects.filter(user_id=request.user)
	context_dict = {}
	item_list = []
	for c in cart:
		itemid = c.product_id
		items = Computer.objects.get(pk=itemid)
		item_list.append(items)

	context_dict = {'items':item_list}
	return render(request,'cart_view.html',context_dict)





