from django.shortcuts import redirect, render
import razorpay
from django.views.decorators.csrf import csrf_exempt

# view function for razor_pay Gateway
def razorpay_payment(request):
    if request.method == "POST":
        amount = 50000
        order_currency = 'INR'
        # ID and SECRET OF RAZORPAY
        client = razorpay.Client(
            auth=("rzp_test_ghNAkp5dg52eOQ", "yOi5MMrBQkBLbZ80ba9ZAA12"))

        payment = client.order.create({'amount': amount,
                                       'currency': 'INR',
                                       'payment_capture': '1'})
        return redirect('/payment/success')
    return render(request, 'index.html')


# view function for success page
@csrf_exempt
def success(request):
    return render(request, "success.html")