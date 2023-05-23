import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QLineEdit, QDialog
from PyQt5.QtTest import QTest

import sys

from main import MainWindow

app = QApplication(sys.argv)


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.window = MainWindow()

    # test admin button
    def test_staff_button_click(self):
        # Find the admin button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the admin button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

    print("MISC STAFF BUTTON CLICK TEST --- PASSED")

    # test customer button
    def test_customer_button_click(self):
        # Find the customer button
        custButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Customer":
                custButton = widget
                break

        # Simulate clicking the customer button
        custButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

    print("MISC CUSTOMER BUTTON CLICK TEST --- PASSED")

    def test_back_button(self):
        # Find the admin button and simulate a click
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Find the backbutton on login page and simulate a back button click
        backButton = None
        for widget in self.window.pageLogin.children():
            if isinstance(widget, QPushButton) and widget.text() == "Back":
                backButton = widget
                break
        backButton.click()

        # Verify that the stacked widget is now on the main page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageMain
        )

        print("MISC BACK BUTTON CLICK TEST --- PASSED")

    ### ADMIN LOGIN SUITE
    def test_admin_login_success(self):
        # Simulate clicking the admin button
        admin_button = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                admin_button = widget
                break
        admin_button.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("admin")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the admin page
        self.assertEqual(self.window.stackedWidget.currentWidget(), self.window.admin)

        print("ADMIN LOGIN SUCCESS TEST --- PASSED")

    def test_admin_login_unsuccess(self):
        # Simulate clicking the admin button
        admin_button = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                admin_button = widget
                break
        admin_button.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("admin")
        self.window.pageLogin.password_edit.setText("wrongpassword")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is not on the admin page
        self.assertNotEqual(
            self.window.stackedWidget.currentWidget(), self.window.admin
        )

        print("ADMIN LOGIN UNSUCCESS TEST --- PASSED")

    def test_admin_manage_account_success(self):
        # Simulate clicking the admin button
        admin_button = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                admin_button = widget
                break
        admin_button.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("admin")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is on the admin page
        self.assertEqual(self.window.stackedWidget.currentWidget(), self.window.admin)

        # Simulate clicking the manage accounts button
        self.window.admin.pushButton1.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.userAdminUI
        )

        print("ADMIN MANAGE ACCOUNTS TEST --- PASSED")

    def test_admin_create_account_success(self):
        # Simulate clicking the admin button
        admin_button = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                admin_button = widget
                break
        admin_button.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("admin")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is on the admin page
        self.assertEqual(self.window.stackedWidget.currentWidget(), self.window.admin)

        # Simulate clicking the manage accounts button
        self.window.admin.pushButton1.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.userAdminUI
        )

        # Simulate clicking the create accounts button
        self.window.userAdminUI.buttonCreateAcc.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.createAccUI
        )

        print("ADMIN CREATE ACCOUNTS TEST --- PASSED")

    def test_admin_create_profile_success(self):
        # Simulate clicking the admin button
        admin_button = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                admin_button = widget
                break
        admin_button.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("admin")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is on the admin page
        self.assertEqual(self.window.stackedWidget.currentWidget(), self.window.admin)

        # Simulate clicking the manage accounts button
        self.window.admin.pushButton1.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.userAdminUI
        )

        # Simulate clicking the create accounts button
        self.window.userAdminUI.buttonCreate2.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.createProfUI
        )

        print("ADMIN CREATE PROFILE TEST --- PASSED")

    ### CUSTOMER LOGIN SUITE
    def test_customer_login_success(self):
        # Find the customer button
        custButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Customer":
                custButton = widget
                break

        # Simulate clicking the customer button
        custButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("customer")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the admin page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.customerUI
        )

        print("CUSTOMER LOGIN SUCCESS TEST --- PASSED")

    def test_customer_login_unsuccess(self):
        # Find the customer button
        custButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Customer":
                custButton = widget
                break

        # Simulate clicking the customer button
        custButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("customer")
        self.window.pageLogin.password_edit.setText("wrongpassword")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the admin page
        self.assertNotEqual(
            self.window.stackedWidget.currentWidget(), self.window.customerUI
        )

        print("CUSTOMER LOGIN UNSUCCESS TEST --- PASSED")

    def test_customer_purchase_tickets_success(self):
        # Find the customer button
        custButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Customer":
                custButton = widget
                break

        # Simulate clicking the customer button
        custButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("customer")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the admin page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.customerUI
        )

        self.window.customerUI.buy_button.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.purchaseTicUI
        )

        print("CUSTOMER PURCHASE TICKETS SUCCESS TEST --- PASSED")

    def test_customer_purchase_fb_success(self):
        # Find the customer button
        custButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Customer":
                custButton = widget
                break

        # Simulate clicking the customer button
        custButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("customer")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the admin page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.customerUI
        )

        self.window.customerUI.buy_food_button.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.purchaseFoodUI
        )

        print("CUSTOMER PURCHASE FOOD SUCCESS TEST --- PASSED")

    def test_customer_accountinfo_success(self):
        # Find the customer button
        custButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Customer":
                custButton = widget
                break

        # Simulate clicking the customer button
        custButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid admin credentials
        self.window.pageLogin.userID_edit.setText("customer")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the admin page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.customerUI
        )

        self.window.customerUI.info_button.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.customerInfoUI
        )

        print("CUSTOMER ACCOUNT INFO SUCCESS TEST --- PASSED")

    ### CINEMA MANAGER LOGIN SUITE
    def test_manager_login_success(self):
        # Find the Staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the Staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid manager credentials
        self.window.pageLogin.userID_edit.setText("manager")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the manager page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.managerUI
        )

        print("CINEMA MANAGER LOGIN SUCCESS TEST --- PASSED")

    def test_manager_login_unsuccess(self):
        # Find the staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter invalid manager credentials
        self.window.pageLogin.userID_edit.setText("manager")
        self.window.pageLogin.password_edit.setText("wrongpassword")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is not on the manager page
        self.assertNotEqual(
            self.window.stackedWidget.currentWidget(), self.window.managerUI
        )

        print("CINEMA MANAGER LOGIN UNSUCCESS TEST --- PASSED")

    def test_manager_movies_success(self):
        # Find the Staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the Staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid manager credentials
        self.window.pageLogin.userID_edit.setText("manager")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the manager page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.managerUI
        )

        self.window.managerUI.moviesButton.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.manageMoviesUI
        )

        print("CINEMA MANAGER MOVIES SUCCESS TEST --- PASSED")

    def test_manager_tickets_success(self):
        # Find the Staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the Staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid manager credentials
        self.window.pageLogin.userID_edit.setText("manager")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the manager page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.managerUI
        )

        self.window.managerUI.ticketsButton.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.manageTicTypeUI
        )

        print("CINEMA MANAGER TICKETS SUCCESS TEST --- PASSED")

    def test_manager_hall_success(self):
        # Find the Staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the Staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid manager credentials
        self.window.pageLogin.userID_edit.setText("manager")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the manager page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.managerUI
        )

        self.window.managerUI.hallButton.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.manageHallsUI
        )

        print("CINEMA MANAGER HALLS SUCCESS TEST --- PASSED")

    def test_manager_food_success(self):
        # Find the Staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the Staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid manager credentials
        self.window.pageLogin.userID_edit.setText("manager")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the manager page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.managerUI
        )

        self.window.managerUI.fbButton.click()

        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.manageFBUI
        )

        print("CINEMA MANAGER FOOD AND BEVERAGE SUCCESS TEST --- PASSED")

    # def test_manager_edit_movie_success(self):
    #     # Find the staff button
    #     adminButton = None
    #     for widget in self.window.pageMain.children():
    #         if isinstance(widget, QPushButton) and widget.text() == "Staff":
    #             adminButton = widget
    #             break

    #     # Simulate clicking the staff button
    #     adminButton.click()

    #     # Verify that the stacked widget is now on the login page
    #     self.assertEqual(
    #         self.window.stackedWidget.currentWidget(), self.window.pageLogin
    #     )

    #     # Enter valid manager credentials
    #     self.window.pageLogin.userID_edit.setText("manager")
    #     self.window.pageLogin.password_edit.setText("password")

    #     # Simulate clicking the login button
    #     self.window.pageLogin.login_button.click()

    #     # Verify that the stacked widget is not on the manager page
    #     self.assertEqual(
    #         self.window.stackedWidget.currentWidget(), self.window.managerUI
    #     )

    #     self.window.managerUI.moviesButton.click()

    #     self.assertEqual(
    #         self.window.stackedWidget.currentWidget(), self.window.manageMoviesUI
    #     )

    #     self.window.manageMoviesUI.editButton.click()

    #     # Verify that the dialog is opened
    #     for widget in self.window.manageMoviesUI.children():
    #         if isinstance(widget, QDialog):
    #             dialog = widget
    #             break
    #     print(dialog)

    #     # Access the widgets in the dialog and edit their values
    #     name_edit = dialog.findChild(QLineEdit, "name_edit")
    #     genre_edit = dialog.findChild(QLineEdit, "genre_edit")
    #     avail_edit = dialog.findChild(QLineEdit, "avail_edit")

    #     name_edit.setText("New Movie Name")
    #     genre_edit.setText("New Genre")
    #     avail_edit.setText("New Availability")

    #     # Simulate clicking the submit button
    #     submit_button = dialog.findChild(QPushButton, "submitButton")
    #     submit_button.click()

    #     # Verify that the dialog is closed
    #     self.assertFalse(dialog.isVisible())

    #     print("CINEMA MANAGER EDIT MOVIE TEST --- PASSED")

    ### CINEMA OWNER LOGIN SUITE
    def test_owner_login_success(self):
        # Find the Staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the Staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid owner credentials
        self.window.pageLogin.userID_edit.setText("owner")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the owner page
        self.assertEqual(self.window.stackedWidget.currentWidget(), self.window.ownerUi)

        print("CINEMA OWNER LOGIN SUCCESS TEST --- PASSED")

    def test_owner_login_unsuccess(self):
        # Find the staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter invalid owner credentials
        self.window.pageLogin.userID_edit.setText("owner")
        self.window.pageLogin.password_edit.setText("wrongpassword")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is not on the manager page
        self.assertNotEqual(
            self.window.stackedWidget.currentWidget(), self.window.ownerUi
        )

        print("CINEMA OWNER LOGIN UNSUCCESS TEST --- PASSED")

    def test_owner_logout_success(self):
        # Find the Staff button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Staff":
                adminButton = widget
                break

        # Simulate clicking the Staff button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Enter valid owner credentials
        self.window.pageLogin.userID_edit.setText("owner")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the owner page
        self.assertEqual(self.window.stackedWidget.currentWidget(), self.window.ownerUi)

        # logout of owner
        self.window.ownerUi.logOutButton.click()
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageMain
        )

        print("CINEMA OWNER LOGOUT SUCCESS TEST --- PASSED")

    def tearDown(self):
        self.window.close()


if __name__ == "__main__":
    unittest.main()
