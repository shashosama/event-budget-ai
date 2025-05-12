from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    try:
        # Read spreadsheet using pandas
        df = pd.read_excel(file) if file.filename.endswith('.xlsx') else pd.read_csv(file)

        # Expecting columns: Category, Amount
        summary = df.groupby('Category')['Amount'].sum().to_dict()
        total = df['Amount'].sum()

        # Simple suggestion logic
        suggestions = []
        if summary.get('Decorations', 0) > 100:
            suggestions.append("Themed Party")
        if summary.get('Food', 0)/total > 0.4:
            suggestions.append("Food-Centric Event")

        return jsonify({
            'total_spent': total,
            'summary': summary,
            'suggestions': suggestions or ["Simple Gathering"]
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
