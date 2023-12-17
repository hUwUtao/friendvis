import sys

# Scrapish
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

# Holy f c-like-struct
from dataclasses import dataclass, asdict, is_dataclass

from threading import Thread

# Out
# from json import dump
import json
import pickle

USER, OUTFS = sys.argv[1], sys.argv[2]


@dataclass
class Ent:
  li: str
  name: str
  shr: int
  img: str


opts = Options()
opts.add_argument("--log-level=1")
opts.add_argument("--headless")

driver = webdriver.Chrome(options=opts)
# display.Image("cc")
driver.get("https://mbasic.facebook.com")
cookies = pickle.load(open("cookies.pickle", "rb"))
for cookie in cookies:
  driver.add_cookie(cookie)
driver.get(f"https://mbasic.facebook.com/{USER}/friends?mutual=1")

friends = []


class DCJSONEncoder(json.JSONEncoder):
  def default(self, o):
    if is_dataclass(o):
      return asdict(o)
    return super().default(o)


def dmpint(stri):
  m = "".join(re.findall("([0-9]*)", stri))
  return int(m) if len(m) > 0 else 0


PTH = f"{OUTFS}/{USER}"
print(f"> {PTH}.json")
def snapfs():
  print(">fs")
  with open(f"{PTH}.json", "w") as fio:
    json.dump(friends, fio, cls=DCJSONEncoder, separators=(",", ":"))
  # with open(f"{PTH}.pickle", "wb") as fio:
  #   pickle.dump(friends, fio)

def ivsnap():
  thread = Thread(target = snapfs, args = ())
  thread.start()

while True:
  root = driver.find_element(By.ID, "root")
  WebDriverWait(driver, 15).until(lambda d: root.is_displayed())
  print("..")
  li = root.find_elements(
    By.CSS_SELECTOR, "table[role=presentation]:has(tbody>tr>td>img)"
  )
  # print("class", once.get_attribute("class"))
  print("+", len(li))
  for r in li:
    # r=i.find_element(By.XPATH, ".//table/tbody/tr")
    rf = dmpint(r.find_element(By.XPATH, ".//td[2]/div[1]").text)
    if rf < 1:
      continue
    friends.append(
      Ent(
        "".join(
          re.findall(
            r"facebook\.com/(?:profile\.php\?id=([0-9]*)|([^=&?]*))",
            r.find_element(By.XPATH, ".//td[2]/a").get_attribute("href"),
          )[0]
        ),
        r.find_element(By.XPATH, ".//td[2]/a").text,
        rf,  # i.find_element(By.XPATH, "//td/div")
        r.find_element(By.XPATH, ".//td[1]/img").get_attribute("src"),
      )
    )
  ivsnap()
  try:
    # print("Await new page and save")
    tpag = driver.find_element(By.ID, "m_more_mutual_friends").find_element(
      By.XPATH, ".//a"
    )
    tpag.click()
    continue
  except:  # noqa: E722
    break

print("X-X")
# snapfs()
