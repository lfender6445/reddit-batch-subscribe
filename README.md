process a batch of subreddits, subscribing to each of them

# setup
1. run `git clone https://github.com/lfender6445/reddit-batch-subscribe`
2. run `cp .env.example .env`
3. edit `.env` to include credentials
4. edit `list.txt` to include the subreddits you want to subscribe to
5. install deps and run the script, see below

```sh
pip3 install -r requirements.txt
python3 batch-subscribe.py
```
