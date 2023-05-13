class ShoppingCart {
    constructor() {
        this.total = 0;
        this.items = {};
    }

    addItem(item_name, quantity, price) {
        // this.items = { item_name:quantity };
        this.items[item_name] = quantity;
        this.total += (quantity * price);
        console.log("Product's name: " + item_name + " Qauntity: " + quantity + " Price: " + price);
    }

    removeItem(item_name, quantity, price) {
        // confusion set it
        var prevQuantity = this.items[item_name];
        if (prevQuantity) {
            if (prevQuantity >= quantity) {
                var currentQuantity = prevQuantity - quantity;
                this.items[item_name] = currentQuantity;
                this.total -= (quantity * price);
            } else {
                delete this.items[item_name];
                this.total -= (prevQuantity * price);
            }
        }
    }

    updateQuantity(item_name, newQuantity) {
        this.items[item_name] = newQuantity;
    }
    getTotalCost() {
        console.log(this.total)
    }
}


let cart = new ShoppingCart();
cart.addItem("Mango", 3, 10);
cart.addItem("Orange", 16, 10);

//------Adding new product-----
/*var newproduct=prompt("Enter new product: ");
var newquantity=prompt("Enter it's quantity: ");
let new_quantity=Number(newquantity);
var newprice=prompt("Enter it's price:");
let new_price=Number(newprice)
cart.addItem(newproduct,new_quantity,new_price); */

//-------Removing item------
/*var product=prompt("Enter the name of product: ");
var quantity=prompt("Enter it's quantity: ");
let Quantity=Number(quantity);
var price=prompt("Enter it's price:");
let Price=Number(price)
cart.removeItem(product,Quantity,Price);*/

//------Adding new quantity---------
/*var name = prompt("Enter product's name:  ");
var quantity = prompt("Enter new quantity:  ");
let num=Number(quantity);
cart.updateQuantity(name, num);*/

//-----Getting total cost-----
//cart.getTotalCost();
