def generate_coupen_code(length=10):
    "generate a alphanumberic coupen code"
    characters = string.ascii_uppercase+string.digits
    while True:
        order_id=' '.join(secret.choice(characters)for _ in range(length))
        if not Coupen.objects.filter(code=order_id).exists():
            return order_id

logger = logging.getLogger(name)
def send_order_confirmation_email(order_id,customer_email,customer_name,items,price):
    
    """
    Args:
    order_id(int),customer_email(str),customer_name(str),items(list),total_price(Decimal)
    Returns:
        dict:{'success':True}or|{'success':False,'error':'...'}
    """

    subject = f"Order Confirmation Order{order_id}"
    item_list = '\n'.join([f"-{item}"for item in items])
    messages ={
        f"hai {customer_name}"
        f"thankyou for order"

    }
    try:
        send_mail(
            subject,message,settings.DEFAULT_FROM_EMAIL,[customer_email],fail_silent=False
        )
        return {'success':True}
    except BadHeaderError:
        logger.error(f"BadErrorHeader sending email{customer_email}{customer_name})
        return{'success':False,'error':'Invalid header found'}
    except Exception as e:
        logger.exception(f"error sending conformation{customer_email})
        return{'success':False,'error':str(e)}


def get_daily_sales(target_date:date):
    """Return total sales report"""
    orders = Order.objects.filter(created__at__date=target_date)
    total = order.aggregate(total_sum=Sum('total_price'))['total_sum']
    return total or 0