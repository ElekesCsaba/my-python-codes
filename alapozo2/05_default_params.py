# positional params
# default params: param_name=default value
def food_order_form(
        first_name,
        last_name,
        phone,
        email,
        food,
        message=None,
        coupon=None
):
    print(f"Thank {first_name} {last_name}.")
    print(f"Food: {food}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

    price = 1000

    if message:
        print(f"Message: {message}")

    if coupon:
        print(f"Total: {price / 2} Ft")
    else:
        print(f"Total: {price} Ft")


# explicit hívás:
food_order_form(
    food="hambi",
    first_name="Elekes",
    last_name="Csaba",
    phone="34567",
    email="email@csaba.hu",
    message="Gyere be!",
    coupon="Action!"
)