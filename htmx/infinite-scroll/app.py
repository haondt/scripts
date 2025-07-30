from flask import Flask, render_template, request

app = Flask(__name__)

# Mock data - in a real app this would come from a database
ITEMS = [f"Item {i}" for i in range(1, 101)]  # 100 items
PAGE_SIZE = 10

@app.route('/')
def index():
    """Main page with initial items"""
    initial_items = ITEMS[:PAGE_SIZE]
    has_more = len(ITEMS) > PAGE_SIZE
    return render_template('index.html',
                         items=initial_items,
                         next_page=1 if has_more else None)

@app.route('/items')
def get_items():
    """HTMX endpoint for infinite scroll"""
    page = int(request.args.get('page', 0))
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE

    items = ITEMS[start:end]
    has_more = end < len(ITEMS)
    next_page = page + 1 if has_more else None

    return render_template('items.html',
                         items=items,
                         next_page=next_page)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
