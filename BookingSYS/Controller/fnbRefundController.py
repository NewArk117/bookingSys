from fnb import FnB

class FnbRefundController:
    def __init__(self, fnb_refund_ui):
        self.fnb_refund_ui = fnb_refund_ui

    def show_food_list(self, order_id):
        food_data = FnB.get_order_items(order_id)
        food_strings = []
        for row in food_data:
            food_string = "Food Name: {}\nQuantity: {}".format(row[0], row[1])
            food_strings.append(food_string)
        self.fnb_refund_ui.food_list.clear()
        self.fnb_refund_ui.food_list.addItems(food_strings)

    def confirm_refund(self):
        selected_items = self.fnb_refund_ui.food_list.selectedItems()

        if len(selected_items) > 0:
            order_id = self.fnb_refund_ui.order_id

            for item in selected_items:
                food_info = item.text().split('\n')
                food_name = food_info[0].split(':')[1].strip()
                quantity = int(food_info[1].split(':')[1].strip())

                FnB.delete_order_item(order_id, food_name, quantity)

            self.show_food_list(order_id)
            self.fnb_refund_ui.stackedWidget.setCurrentIndex(8)
