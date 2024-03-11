def discounted_price(price_list,discount,index):
    d_price = price_list[index]-(price_list[index] * (discount / 100))
    return d_price

p_list = [17,25,1000,58]
print(float(round(discounted_price(p_list,56,1))))
