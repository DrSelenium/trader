from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/trading-bot', methods=['POST'])
def trading_bot():
    data = request.get_json()
    results = []
    for event in data:
        id = event['id']
        title = event['title'].lower()
        # simple sentiment analysis
        positive_words = ['bullish', 'rise', 'up', 'gain', 'increase', 'positive', 'good', 'buy', 'long', 'pump', 'moon', 'trump', 'executive', 'order', 'reserve']
        negative_words = ['bearish', 'fall', 'down', 'drop', 'decrease', 'negative', 'bad', 'sell', 'short', 'dump', 'crash']
        score = 0
        for word in positive_words:
            if word in title:
                score += 1
        for word in negative_words:
            if word in title:
                score -= 1
        # check previous candles trend
        previous = event.get('previous_candles', [])
        if len(previous) >= 2:
            last_close = previous[-1]['close']
            first_close = previous[0]['close']
            if last_close > first_close:
                score += 0.5
            else:
                score -= 0.5
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
    app.run()
