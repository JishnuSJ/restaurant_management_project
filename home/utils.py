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

def is_resturant_open():
    """Return check open or not """
    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()
    opening_hours = {
        0:(time(9,0),time(22,0)),#monday
        1:(time(9,0),time(22,0)),#tuesday
        6:(time(90),time(22,0)),#sunday

    }
    open_time,close_time = opening_hours.get(current_day)
    return open_time <= current_time <= close_time


def calculate_discount(item):
    if orginal_price<0:
        raise ValueError("not neg")
    if not(0<=discount_percentage<=100):
        raise ValueError("Discount percentage 0 and 100")
    if item.discount_code:
        return item.price*Decimal('0.09')
    if ordder_total<0 or discount_percentage<0:
        raise ValueError("input neg")
    return round(ordder_total*(discount_percentage/100),2)
    return item.price

    
def update_oredre_status(order_id,new_status):
    order = Order.objects.get(id=order_id)
    old_status = order.status
    order.status = new_status
    order.save()
    return True,f"Order{order.id}status update to'new status'"

def calculate_oredr(order_items):
    for item in order_items:
        qua=item.get('qua',0)
        price=item.get('price',0)
    return round(total,2)

def is_valid_email(email):
    if not isinstance(email,str):
        return False
    email_regex=r'[a-zA-Z0-9]+@