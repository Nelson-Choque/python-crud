from fastapi import FastAPI
from typing import List
from product import Product


# //* create server 
app = FastAPI();

# //* set list initial

productList:List[Product] = []

# add inital elements
product: Product = Product(id=2,name="name example",price=120)
productList.append(product)

# //* ********* route product ********
@app.get("/")
def product_all():

    return {"products":productList}


@app.post("/")
def product_create(product:Product):
    
    # //* add element 
    productList.append(product)
    return productList

@app.put("/:{id}")
def product_edit(id:int,newProduct:Product):

    product:Product = None
    
    # // * find element
    
    for item in productList:

        if(item.id == id):
            product = item
            break
        
    if(product is None):
        return "no se encontro producto con ese id"
    
    # //set same id
    
    newProduct.id = product.id
    
    # // find index
    
    index:int = productList.index(product)
    
    # // replace element
    productList[index] = newProduct
    return productList

@app.delete("/:{id}")
def product_delete(id:int):
    

    product:Product = None
    
    # //* find element 
    for item in productList:

        if(item.id == id):
            product = item
            break
    #// validate is none
    if(product is None):
        return "no se encontro producto con ese id"
    
    #// remove element
    
    productList.remove(product)
    return productList
    

    

    
    