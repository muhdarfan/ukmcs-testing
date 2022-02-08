import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AddCitraCourseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'E:\Projects\Python\ukmcs-testing\Browsers\chromedriver.exe')
        cls.driver.implicitly_wait(10)

        # Login
        cls.driver.get('https://ukmcs.dev/login')
        cls.driver.find_element(By.NAME, 'matric_no').send_keys('D174652')
        cls.driver.find_element(By.NAME, 'password').send_keys('password')
        cls.driver.find_element(By.ID, 'submitBtn').click()

    # Browse to Add Citra Courses page
    def setUp(self):
        self.driver.get('https://ukmcs.dev/citra/create')

    def test_tc_012_009_cancel_send(self):
        driver = self.driver

        driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div/div/form/div[2]/a').click()
        self.assertEqual('https://ukmcs.dev/citra', driver.current_url)
        time.sleep(3)

    def test_tc_012_006_valid_course(self):
        driver = self.driver

        driver.find_element(By.NAME, 'courseCode').send_keys('LMCA1514')
        driver.find_element(By.NAME, 'courseName').send_keys('PENGURUSAN KEWANGAN')
        driver.find_element(By.NAME, 'courseCredit').send_keys('2')
        driver.find_element(By.NAME, 'courseAvailability').send_keys('20')
        driver.find_element(By.NAME, 'descriptions').send_keys('Course that help student manage financial')
        driver.find_element(By.CLASS_NAME, 'btn-success').click()

        assert "Citra Courses created successfully." in driver.page_source

    def test_tc_012_007_taken_course_code(self):
        driver = self.driver

        self.assertIn("Add Course", self.driver.page_source)

        driver.find_element(By.NAME, 'courseCode').send_keys('LMCA1402')
        driver.find_element(By.CLASS_NAME, 'btn-success').click()
        time.sleep(3)

        assert "The course code has already been taken." in driver.page_source

    def test_tc_012_008_invalid_availability(self):
        driver = self.driver

        driver.find_element(By.NAME, 'courseAvailability').send_keys('0')
        driver.find_element(By.CLASS_NAME, 'btn-success').click()
        time.sleep(3)

        assert "The course availability must be at least 1." in driver.page_source

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
