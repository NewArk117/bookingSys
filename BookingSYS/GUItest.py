import unittest
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
)
import sys

from main import MainWindow

app = QApplication(sys.argv)


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.window = MainWindow()

    # test admin button
    def test_admin_button_click(self):
        # Find the admin button
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Admin":
                adminButton = widget
                break

        # Simulate clicking the admin button
        adminButton.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Verify that the account type is set to admin
        self.assertEqual(self.window.pageLogin.acctype, "admin")

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

        # Verify that the account type is set to customer
        self.assertEqual(self.window.pageLogin.acctype, "customer")

    def test_admin_login_success(self):
        # Simulate clicking the admin button
        admin_button = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Admin":
                admin_button = widget
                break
        admin_button.click()

        # Verify that the stacked widget is now on the login page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.pageLogin
        )

        # Verify that the account type is set to admin
        self.assertEqual(self.window.pageLogin.acctype, "admin")

        # Enter valid admin credentials
        self.window.pageLogin.username_edit.setText("admin")
        self.window.pageLogin.password_edit.setText("password")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the admin page
        self.assertEqual(self.window.stackedWidget.currentWidget(), self.window.admin)

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

        # Verify that the account type is set to customer
        self.assertEqual(self.window.pageLogin.acctype, "customer")

        # Enter valid admin credentials
        self.window.pageLogin.username_edit.setText("fjwxs701")
        self.window.pageLogin.password_edit.setText("xaKehNOH")

        # Simulate clicking the login button
        self.window.pageLogin.login_button.click()

        # Verify that the stacked widget is now on the admin page
        self.assertEqual(
            self.window.stackedWidget.currentWidget(), self.window.customerUI
        )

    def test_back_button(self):
        # Find the admin button and simulate a click
        adminButton = None
        for widget in self.window.pageMain.children():
            if isinstance(widget, QPushButton) and widget.text() == "Admin":
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

    def tearDown(self):
        self.window.close()


if __name__ == "__main__":
    unittest.main()
