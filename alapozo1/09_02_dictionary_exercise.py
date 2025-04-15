business_key_list = {}
bk_fields = "Product_name, Buyer_name, Shop_name"
scd1_fields = "Money_key, Order_id, Shipping_type"
scd2_fields = "Delivery_status, Home_type, Home_street_name, Order_id"

list1 = bk_fields.split(",")
list2 = scd1_fields.split(",")
list3 = scd2_fields.split(",")

list1.extend(list2)
list1.extend(list3)

for i in list1:
    business_key_list[i.strip()] = 9

print(len(list1))
print(len(business_key_list))
