import csv
from os import listdir, argv
from json import load as jload

with open("deffs.csv", "w", newline="") as dio:
  gfs = csv.writer(dio)
  gfs.writerow(["id", "name", "si"])
  with open(f"data/{argv[1]}.json", "r") as fio:
    for i in jload(fio):
      gfs.writerow([i["li"], i["name"], i["shr"]])


with open("treefs.csv", "w", newline="") as gio:
  gfs = csv.writer(gio)
  gfs.writerow(["l", "r"])
  for i in listdir("./data/child"):
    n = i[0:-5]
    with open(f"./data/child/{i}", "r") as fio:
      for ii in jload(fio):
        gfs.writerow([n, ii["li"]])
