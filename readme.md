## FriendVis

A workflow to pipe mutual friend using Facebook old interface

### req

- A Facebook acount that temporary unlock 2FA
- `python>=3.10` if you don't dare
- `pypy>=3.10` optional if you want to bake csv faster for larger and complex friend list
- `jq`
- `msys2` (windows only)

#### `python` profile (for stable scraping, and stun itself too, required)

- `selenium`

#### `pypy`/`python` profile (for fast processing, recommend using colab)

- `pandas`

### setup

- right creds

```sh
# .env
FB_USER=chinchon@binbon.co
FB_PASS=yikes_this_is_unreal
```

- bake cookies

```sh
python login.py
```

- scrape (round 1)

```sh
bash ./init.sh
```

- turn on your 2fa back if you prefer

### bake csv (squashier json files)

- `pypy mkcsv.py`/`python mkcsv.py`

### last step (choose 1/3)

- upload all csv files to colab, tweaking things to work (you nerdy way)
- on windows, install mvcc and pandas (sucks)
- on linux, ignore

then

- install pandas
- run vis.py