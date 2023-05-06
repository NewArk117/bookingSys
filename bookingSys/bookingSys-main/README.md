# bookingSys

Pre requesite

pyqt installed <<< you can use "pip install pyqt
                                pip install pyqt-tools"

change "sys.path.append()" path to the correct one that matches your directory

step 1: at the main directory use python main.py


Boundary is for UI's, where it is the interface for all the buttons etc.
Controller is for the UI's button to call.
Entity will then be called by controller, which does all the functional stuff(SQL, checks, control etc.)

E.g. To create an account

manageAcc.py (found in boundary) has a button "Create account".
1) Create a UI for taking in the account information (createAccUI.py)
2) In createAccUI.py, it takes in the information for the new account, and creates a function
    "createAccount(self)" which takes the information of the account and parses it into the controller (createAccountController.py in Controller folder)
3) Controller calls the Entity function, and parses the information into the Entity(accCreate.py in Entity folder)
4) Entity is where we should process the sql and create the account in the DB
5) Add your newly created UI into main.py, find comment "CREATE OBJECT OF UI HERE" and copy the format of create a new object.
6) The comment number beside the object is the index for that page.
7) Notice that in manageAcc.py, the "goCreateAcc" function has "self.stackedWidget.setCurrentIndex(5)", this line basically tells the system
    to go to the widget(a page) that was stacked (did it in main.py, where you added the object into the stackedWidget, each object stacked should be the UI.).
    index(5) is the create account page