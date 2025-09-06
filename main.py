from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/trading-bot', methods=['POST'])
def trading_bot():
    data = request.get_json()
    results = []
    for event in data:
        id = event['id']
        title = event['title'].lower()
        # enhanced sentiment analysis with weights
        positive_words = {
            'bullish': 2, 'rise': 1, 'up': 1, 'gain': 1, 'increase': 1, 'positive': 1, 'good': 1, 'buy': 1, 'long': 1, 'pump': 1, 'moon': 1,
            'trump': 2, 'executive': 1, 'order': 1, 'reserve': 1, 'surge': 1, 'rally': 1, 'breakthrough': 1, 'partnership': 1, 'investment': 1,
            'adoption': 1, 'halving': 2, 'institutional': 1, 'approval': 1, 'green': 1, 'support': 1, 'optimism': 1, 'growth': 1, 'boom': 1
        }
        negative_words = {
            'bearish': 2, 'fall': 1, 'down': 1, 'drop': 1, 'decrease': 1, 'negative': 1, 'bad': 1, 'sell': 1, 'short': 1, 'dump': 1, 'crash': 2,
            'ban': 2, 'regulation': 1, 'sell-off': 1, 'decline': 1, 'plunge': 1, 'warning': 1, 'concern': 1, 'fear': 1, 'panic': 1, 'red': 1,
            'opposition': 1, 'rejection': 1, 'downturn': 1, 'slump': 1
        }
        score = 0
        for word, weight in positive_words.items():
            if word in title:
                score += weight
        for word, weight in negative_words.items():
            if word in title:
                score -= weight
        # check for emphasis
        if '!' in title or title.isupper():
            score *= 1.5  # amplify sentiment if emphasized
        # enhanced trend analysis
        previous = event.get('previous_candles', [])
        if len(previous) >= 2:
            first_close = previous[0]['close']
            last_close = previous[-1]['close']
            pct_change = (last_close - first_close) / first_close * 100
            if pct_change > 1:
                score += 1
            elif pct_change < -1:
                score -= 1
            # also check volume trend
            if len(previous) > 1:
                avg_volume = sum(c['volume'] for c in previous) / len(previous)
                last_volume = previous[-1]['volume']
                if last_volume > avg_volume * 1.2:
                    score += 0.5  # high volume might indicate strong move
        if score > 0:
            decision = 'LONG'
        elif score < 0:
            decision = 'SHORT'
        else:
            decision = 'LONG'  # default
        results.append({'id': id, 'decision': decision, 'score': abs(score)})
    # select top 50 by score
    results.sort(key=lambda x: x['score'], reverse=True)
    selected = results[:50]
    response = [{'id': r['id'], 'decision': r['decision']} for r in selected]
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=False)