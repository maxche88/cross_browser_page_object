from testpage import OperationHelper
import yaml
import logging
import time

with open("./testdata.yaml") as f:
    data = yaml.safe_load(f)


class TestPN:
    def test_step1(self, run_browser):
        logging.info("test_step1 Starting")
        testpage = OperationHelper(run_browser)
        testpage.go_to_site()
        testpage.enter_login("test")
        testpage.enter_pass("test")
        testpage.click_login_button()
        assert testpage.get_error_text() == "401", "FAIL"

    def test_step2(self, run_browser):
        logging.info("test_step2 Starting")
        testpage = OperationHelper(run_browser)
        testpage.enter_login(data['name'])
        testpage.enter_pass(data['pass'])
        testpage.click_login_button()
        assert testpage.get_label_text() == f"Hello, {data['name']}", "FAIL"

    def test_step3(self, run_browser, random_text):
        logging.info("test_step3 Starting")
        rnd_text = random_text
        testpage = OperationHelper(run_browser)
        testpage.click_create_new_post_btn()
        testpage.enter_title(rnd_text)
        testpage.enter_description(rnd_text)
        testpage.enter_content(rnd_text)
        testpage.click_save_post_btn()
        assert testpage.get_title_post() == rnd_text, "FAIL"

    def test_step4(self, run_browser, random_text):
        logging.info("test_step4 Starting")
        rnd_text = random_text
        testpage = OperationHelper(run_browser)
        testpage.click_contact_btn()
        testpage.enter_your_name(rnd_text)
        testpage.enter_your_email(f'{rnd_text}@{rnd_text}.bk')
        testpage.enter_your_content(rnd_text)
        testpage.click_contact_us_btn()
        res = testpage.get_alert()
        logging.info("alert" + res.text)
        assert res, "FAIL"



