customers_database = {
    "customer-1": "AX-123",
    "customer-2": "BX-123",
    "customer-3": "CX-123",
    "customer-4": "DX-123",
    "customer-5": "EX-123",
}
cost_per_unit = 2
number_of_units = 5


class ProductEvent:

    def __init__(self, event_type, product_number, timestamp):
        self.event_type = event_type
        self.product_number = product_number
        self.timestamp = timestamp


class BillingEvent:

    def __init__(self, customer_id, product_number, pickup_time, purchase_time, shopping_cost):
        self.customer_id = customer_id
        self.product_number = product_number
        self.pickup_time = pickup_time
        self.purchase_time = purchase_time
        self.shopping_cost = shopping_cost
