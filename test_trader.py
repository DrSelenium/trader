import requests
import json

# Sample data from the example
data = [
    {
        "id": 1,
        "title": "db (@tier10k): *TRUMP SIGNS EXECUTIVE ORDER TO ESTABLISH STRATEGIC BITCOIN RESERVE: SACKS",
        "time": 1741306326681,
        "url": "https://twitter.com/tier10k/status/1897802400632648066",
        "source": "Twitter",
        "previous_candles": [
            {
                "timestamp": 1741306200000,
                "open": 89886.67,
                "high": 89961.27,
                "low": 89878.51,
                "close": 89960.51,
                "volume": 4.85351,
                "datetime": "2025-03-07 08:10:00"
            },
            {
                "timestamp": 1741306260000,
                "open": 89960.52,
                "high": 90229.97,
                "low": 89932.45,
                "close": 90218.6,
                "volume": 62.09979,
                "datetime": "2025-03-07 08:11:00"
            },
            {
                "timestamp": 1741306320000,
                "open": 90218.59,
                "high": 90595.72,
                "low": 90208.24,
                "close": 90591.18,
                "volume": 93.9068,
                "datetime": "2025-03-07 08:12:00"
            }
        ],
        "observation_candles": [
            {
                "timestamp": 1741306380000,
                "open": 90591.19,
                "high": 91283.02,
                "low": 90591.19,
                "close": 91123.95,
                "volume": 278.03794,
                "datetime": "2025-03-07 08:13:00"
            },
            {
                "timestamp": 1741306440000,
                "open": 91123.94,
                "high": 91212.0,
                "low": 90218.0,
                "close": 90218.0,
                "volume": 218.40361,
                "datetime": "2025-03-07 08:14:00"
            },
            {
                "timestamp": 1741306500000,
                "open": 90218.0,
                "high": 90420.0,
                "low": 88300.0,
                "close": 89218.58,
                "volume": 720.8261,
                "datetime": "2025-03-07 08:15:00"
            }
        ]
    },
    {
        "id": 2,
        "title": "Bitcoin crashes after bad news",
        "time": 1741306326681,
        "url": "https://example.com",
        "source": "News",
        "previous_candles": [
            {
                "timestamp": 1741306200000,
                "open": 90000.0,
                "high": 90000.0,
                "low": 90000.0,
                "close": 90000.0,
                "volume": 10.0,
                "datetime": "2025-03-07 08:10:00"
            }
        ],
        "observation_candles": []
    },
    {
        "id": 3,
        "title": "Bullish on Bitcoin future",
        "time": 1741306326681,
        "url": "https://example.com",
        "source": "News",
        "previous_candles": [
            {
                "timestamp": 1741306200000,
                "open": 90000.0,
                "high": 90000.0,
                "low": 90000.0,
                "close": 90000.0,
                "volume": 10.0,
                "datetime": "2025-03-07 08:10:00"
            }
        ],
        "observation_candles": []
    }
]

# Send POST request
url = 'http://127.0.0.1:5000/trading-bot'
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

print('Status Code:', response.status_code)
print('Response:', response.json())
