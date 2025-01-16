# e2e.py
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(app_url):
    """Test the scores web service"""
    try:
        driver = webdriver.Chrome()
        driver.get(app_url)

        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text

        try:
            score = int(score_text)
            return 1 <= score <= 1000
        except ValueError:
            return False

    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False
    finally:
        driver.quit()


def main_function():
    """Main function to run tests"""
    if test_scores_service("http://localhost:8777"):
        return 0
    return -1


if __name__ == "__main__":
    exit(main_function())