import sqlite3
from PyQt5.QtWidgets import QMessageBox

class userRegController:
    def process_registration(self, dialog, id, username, password, confirm_password):
        if password == confirm_password:
            # Connect to thedatabase
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()
            try:
                # Check if ID already exists
                cursor.execute("SELECT * FROM account WHERE userID=?", (id,))
                if cursor.fetchone():
                    QMessageBox.critical(dialog, 'Error', 'ID already exists. Please enter a new ID.')
                else:
                    # Check if username already exists
                    cursor.execute("SELECT * FROM account WHERE userName=?", (username,))
                    if cursor.fetchone():
                        QMessageBox.critical(dialog, 'Error', 'Username already exists.')
                    else:
                        # Insert registration details into the database
                        cursor.execute(
                            "INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)",
                            (id, username, password, 'customer'))
                        conn.commit()

                        # Registration successful
                        QMessageBox.information(dialog, 'Success', 'Registration successful.')
                        dialog.accept()
            except Exception as e:
                # Handle database errors
                QMessageBox.critical(dialog, 'Error', 'An error occurred during registration: {}'.format(str(e)))
        else:
            # Passwords do not match
            QMessageBox.critical(dialog, 'Error', 'Passwords do not match.')



