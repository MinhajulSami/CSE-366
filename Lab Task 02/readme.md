Percepts:
The agent receives two percepts:
• Price: The current price of a specific smartphone model.
• Amount in Stock: The quantity of smartphone models available in the store.

Decision Process:
• The agent’s goal is to optimize stock levels while minimizing costs.
• It must decide whether to order more smartphones and, if so, how many to order.

Decision Rules:
• If the price of the smartphone drops significantly (indicating a deal or promotion),
the agent considers ordering more units.

Threshold: Let’s say the threshold is a 20% discount from the average price.
• If the amount in stock falls below a certain level (e.g., 10 units), the agent prioritizes
restocking.
• Otherwise, the agent decides not to place an order.

Commands/Actions:
• If the smartphone price is below the threshold (20% discount) and the stock level is
not critically low, the agent orders a specific quantity (let’s call it tobuy).

Example: If the smartphone price drops to 500 BDT (from an average of 600 BDT) and there
are 20 units in stock, the agent might decide to order 15 more units.
• If the stock level is critical, (e.g., less than 10), the agent orders a minimum quantity
(e.g., 10 units).
• Otherwise, if neither condition is met, the agent does not place an order (i.e., tobuy
= 0).
