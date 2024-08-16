import pandas as pd

# Read Excel file with relative file path
df = pd.read_excel('C:\\Users\\dell\\Documents\\InventoryData.xlsx')


def djb2(product,size):
  hash = 5381
  for i in product:
    hash = ((hash << 5) + hash) + ord(i)
  return hash%size

def rehash(old_hash,size,iteration):
 return (old_hash + iteration**2) % size

def put(keys,values,products, price, size, count):
    # checking if resize is needed
    if count > size * 0.5:
         size = size * 2.3
         print(size)
         new_keys = [None] * size
         new_values = [None] * size
         for i in range(len(keys)):
             if keys[i] is not None:
                 put(new_keys, new_values, [keys[i]], [values[i]], size, 0)
         keys, values = new_keys, new_values
        
    
    for i in range(len(products)):
      hash_value=djb2(products[i],size)
  
      if keys[hash_value] == None:
        keys[hash_value] = products[i]
        values[hash_value] = price[i]
        count+=1
      else:
        if keys[hash_value] == products[i]:
          values[hash_value] = price[i]
        else:
          iteration=1
          next_hash = rehash(hash_value,size,iteration)
          
          while keys[next_hash] != None and keys[next_hash] != products[i]:
            iteration+=1
            next_hash = rehash(hash_value, size, iteration)
          if keys[next_hash] == None:
            keys[next_hash] = products[i]
            values[next_hash] = price[i]
            count+=1
            hash_value = next_hash  # update hash_value to the new slot
          else:
            values[next_hash] = price[i]

def get(keys,values,key, size):
    hash_value = djb2(key, size)
    if keys[hash_value] == key:
        return values[hash_value]
    else:
        iteration = 1
        next_hash = rehash(hash_value, size, iteration)
        while keys[next_hash] != key:
            iteration += 1
            next_hash = rehash(hash_value, size, iteration)
            if keys[next_hash] is None:
                return None
        return values[next_hash]


def bubble_sort(cart):
    if len(cart)==1:
      return cart 
      # print(cart)
    preference=input('How do you want to sort yout bill? Choose one: price or quantity')
    if preference=='price':
      for i in range(0,len(cart)-1):
        for j in range(len(cart)-i-1):
            if j!=(len(cart))-2 and cart[j][2]>cart[j+1][2]:
                cart[j],cart[j+1]=cart[j+1],cart[j]
      return cart
    else:
      for i in range(0,len(cart)-1):
          for j in range(len(cart)-i-1):
              if j!=(len(cart))-2 and cart[j][2]>cart[j+1][2]:
                  cart[j],cart[j+1]=cart[j+1],cart[j]
      # print(cart)
      return cart


def inventory(df):
    count=0
    Total=0
    size=int(1371)
    keys=[None]*size
    values=[None]*size
    products=df["ProductName"]
    price=df["RetailPrice"]
    put(keys,values,products,price,size,count)

    cart=[]
    lst_items=[]
    user_item=input('Enter your items as "2:Bread". Once you are done, enter "Done"')
    grocery= user_item.split(':')
    quantity=int(grocery[0])
    lst=grocery[1:]
    item=''
    for i in lst:
      item+= ''+i
    individual_price=get(keys,values,item,size)
    if individual_price==None:
      return 'This product does not exist in the inventory'
    final_price=round((float(individual_price)*int(quantity)),2)
    Total += final_price
    t=(item, quantity, final_price)
    cart.append(t)

    while user_item!='Done':
      user_item=input()
      if user_item=='Done':
        break
      grocery= user_item.split(':')
      quantity=int(grocery[0])
      lst=grocery[1:]
      item=''
      for i in lst:
        item+= ''+i
      if item!='':
        individual_price=get(keys,values,item,size)
        if individual_price==None:
          return 'This product does not exist in the inventory'
        final_price=round((float(individual_price)*int(quantity)),2)
        Total += final_price
        # print(Total,'total')
        t=(item, quantity, final_price)
        cart.append(t)

    cart.append(round(Total,2))


    return bubble_sort(cart)

print(inventory(df))