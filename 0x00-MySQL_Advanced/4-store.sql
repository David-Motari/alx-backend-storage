-- script that creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER subQuantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET items.quantity = items.quantity - NEW.number
WHERE NEW.item_name  = items.name;


