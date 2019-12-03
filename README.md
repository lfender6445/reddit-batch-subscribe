process a batch of subreddits, subscribing to each of them

# setup
1. run `cp .env.example .env`
2. edit `.env` to include credentials
3. edit `list.txt` to include the subreddit you want to subscribe to
4. install deps and run the script, see below

```python3
pip3 install -r requirements.txt
python3 batch-subscribe.py
```
