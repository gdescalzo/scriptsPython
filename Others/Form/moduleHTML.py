from flask import Flask, render_template, request, redirect, url_for
import modulePostgreSQL

app = Flask(__name__)

# Route to display the form
@app.route('/')
def form():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    country = request.form['country']
    population = request.form['population']
    area = request.form['area']

    # Insert record into PostgreSQL database
    success = modulePostgreSQL.insert_record(name, country, population, area)

    if success:
        # Redirect back to the form after successful submission
        return redirect(url_for('form', success=True))
    else:
        return 'Failed to insert record.'

if __name__ == '__main__':
    app.run(debug=True)
