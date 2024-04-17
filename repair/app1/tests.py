from django.test import TestCase


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import unittest

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()  # Initialize your WebDriver
#         self.driver.get("http://127.0.0.1:8000/login/")  # Replace with your login page URL

#     def test_valid_login(self):
#         username = "Marya"
#         password = "Ma1X2#2"

#         # Find username and password fields
#         username_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "username"))  # Update with your username field locator
#         )
#         password_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "password"))  # Update with your password field locator
#         )

#         # Enter username and password
#         username_field.send_keys(username)
#         password_field.send_keys(password)

#         # Trigger change events after entering username and password
#         self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", username_field)
#         self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", password_field)

#         # Find and click the login button
#         login_button = WebDriverWait(self.driver, 30).until(
#             EC.element_to_be_clickable((By.ID, "loginButton"))  # Update with your login button locator
#         )
#         login_button.click()

#         # Add assertions to verify successful login
#         expected_url = "technician_profile/"
#         self.assertIn(expected_url, self.driver.current_url)  # Update with assertion to check if expected_url is present in the current URL
#     def tearDown(self):
#         self.driver.quit()

# if __name__ == "_main_":
#     unittest.main()


# .......................availability............................................................................


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import unittest
# import time

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/login/")

#     def test_valid_login_and_navigate_to_availability(self):
#         # Replace with your actual username and password
#         username = "Marya"
#         password = "Ma1X2#2"

#         # Find username and password fields
#         username_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "username"))
#         )
#         password_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "password"))
#         )

#         # Enter username and password
#         username_field.send_keys(username)
#         password_field.send_keys(password)

#         # Trigger change events after entering username and password
#         self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", username_field)
#         self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", password_field)

#         # Find and click the login button
#         login_button = WebDriverWait(self.driver, 30).until(
#             EC.element_to_be_clickable((By.ID, "loginButton"))
#         )
#         login_button.click()

#         # Navigate to the Technician Availability page
#         availability_link = WebDriverWait(self.driver, 30).until(
#             EC.element_to_be_clickable((By.ID, "availabilityLink"))
#         )
#         availability_link.click()

#         # Locate the date and availability fields
#         date_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "date"))
#         )
#         availability_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "availability"))
#         )

#         # Enter date and availability
#         date_value = "21-12-2023"  # Replace with your desired date
#         availability_value = "FullDay"  # Replace with your desired availability
#         date_field.send_keys(date_value)
#         availability_field.send_keys(availability_value)

#         # Locate and click the submit button
#         submit_button = WebDriverWait(self.driver, 20).until(
#             EC.element_to_be_clickable((By.ID, "submitBtn"))
#         )
#         submit_button.click()

#         # You can add further assertions or checks if needed

#     def tearDown(self):
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()


# ........................................change password.............................................................


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/login/")

    def test_valid_login_and_navigate_to_change_password(self):
        # Replace with your actual username and password
        username = "Marya"
        password = "Ma1X2#2"

        # Find username and password fields
        username_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "password"))
        )

        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Trigger change events after entering username and password
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", username_field)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", password_field)

        # Find and click the login button
        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "loginButton"))
        )
        login_button.click()

        # Navigate to My Profile dropdown using explicit wait
        my_profile_dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "My Profile"))
        )
        my_profile_dropdown.click()

        # Introduce a delay to make it visible (optional, for demonstration purposes)
        time.sleep(2)

        # Locate and click the Change Password link inside the dropdown using ID
        change_password_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "changePasswordLink"))
        )
        change_password_link.click()

        # Introduce a delay to make it visible (optional, for demonstration purposes)
        time.sleep(2)

        # Locate form elements by ID
        current_password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "current-password"))
        )
        new_password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "new-password"))
        )
        confirm_password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "confirm-password"))
        )

        # Enter values into the form fields
        current_password_field.send_keys("Ma1X2#1")
        new_password_field.send_keys("Ma1X2#2")
        confirm_password_field.send_keys("Ma1X2#2")  # Assuming confirmation matches new password

        # Introduce a delay to make it visible (optional, for demonstration purposes)
        time.sleep(2)

        # Locate and click the submit button by ID
        submit_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "submitBtn"))
        )
        submit_button.click()

        # Introduce a delay to make it visible (optional, for demonstration purposes)
        time.sleep(5)

        # You can add further assertions or checks if needed

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


# .....................................booking...............................................




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import unittest
# import time

# class LoginAndBookingTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/login/")

#     def test_valid_login_and_navigate_to_booking(self):
#         username = "Keerthi"
#         password = "Ka1X2#"

#         # Find username and password fields
#         username_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "username"))
#         )
#         password_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "password"))
#         )

#         # Enter username and password
#         username_field.send_keys(username)
#         password_field.send_keys(password)

#         # Trigger change events after entering username and password
#         self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", username_field)
#         self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", password_field)

#         # Find and click the login button
#         login_button = WebDriverWait(self.driver, 30).until(
#             EC.element_to_be_clickable((By.ID, "loginButton"))
#         )
#         login_button.click()

#         time.sleep(5)

#         # Add assertions to verify successful login
#         expected_url = "customer_profile/"
#         self.assertIn(expected_url, self.driver.current_url)

#         # Navigate to the booking page
#         # Locate and click the "Book Service" link by ID
#         booking_link = WebDriverWait(self.driver, 30).until(
#             EC.element_to_be_clickable((By.ID, "bookServiceLink"))
#         )
#         booking_link.click()

#         time.sleep(5)

#         # Add assertions or checks for successful navigation to the booking page if needed
#         expected_booking_url = "booking/"
#         self.assertIn(expected_booking_url, self.driver.current_url)

#         # Fill out the booking form
#         fullname_field = self.driver.find_element(By.ID, "fullname")
#         fullname_field.send_keys("John Doe")

#         phone_field = self.driver.find_element(By.ID, "phone")
#         phone_field.send_keys("9496446188")

#         service_dropdown = self.driver.find_element(By.ID, "service")
#         service_dropdown.send_keys("AC Repairer")

#         district_dropdown = self.driver.find_element(By.ID, "district")
#         district_dropdown.send_keys("Thiruvananthapuram")

#         date_field = self.driver.find_element(By.ID, "date")
#         date_field.send_keys("21-12-2023")

#         description_field = self.driver.find_element(By.ID, "description")
#         description_field.send_keys("This is a test booking.")

#         # Click the submit button
#         submit_button = self.driver.find_element(By.ID, "submitButton")
#         submit_button.click()

#         time.sleep(5)

#         # Add assertions or checks for successful form submission if needed

#     def tearDown(self):
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import unittest

# class LoginAndBookingTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/login/")

#     def test_valid_login_and_navigate_to_booking(self):
#         username = "Keerthi"
#         password = "Ka1X2#"

#         # Find username and password fields
#         username_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "username"))
#         )
#         password_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "password"))
#         )

#         # Enter username and password
#         username_field.send_keys(username)
#         password_field.send_keys(password)

#         # Find and click the login button
#         login_button = WebDriverWait(self.driver, 30).until(
#             EC.element_to_be_clickable((By.ID, "loginButton"))
#         )
#         login_button.click()

#         # Add assertions to verify successful login
#         expected_url = "customer_profile/"
#         self.assertIn(expected_url, self.driver.current_url)

#         # Navigate to the booking page
#         # Locate and click the "Book Service" link by ID
#         booking_link = WebDriverWait(self.driver, 30).until(
#             EC.element_to_be_clickable((By.ID, "bookServiceLink"))
#         )
#         booking_link.click()

#         # Add assertions or checks for successful navigation to the booking page if needed
#         expected_booking_url = "booking/"
#         self.assertIn(expected_booking_url, self.driver.current_url)

#         # Fill out the booking form
#         fullname_field = WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.ID, "fullname"))
#         )
#         fullname_field.send_keys("John Doe")

#         phone_field = self.driver.find_element(By.ID, "phone")
#         phone_field.send_keys("9496446188")

#         service_dropdown = self.driver.find_element(By.ID, "service")
#         service_dropdown.send_keys("AC Repairer")

#         district_dropdown = self.driver.find_element(By.ID, "district")
#         district_dropdown.send_keys("Thiruvananthapuram")

#         date_field = self.driver.find_element(By.ID, "date")
#         date_field.send_keys("21-12-2023")

#         description_field = self.driver.find_element(By.ID, "description")
#         description_field.send_keys("This is a test booking.")

#         # Find and click the submit button with waiting
#         submit_button = WebDriverWait(self.driver, 30).until(
#             EC.element_to_be_clickable((By.ID, "submitButton"))
#         )
#         submit_button.click()

#         # Add assertions or checks for successful form submission if needed

#     def tearDown(self):
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()
