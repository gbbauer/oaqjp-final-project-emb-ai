# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask("Part Two")

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

def get_transaction_total () :
    total = float(0)

    for transaction in transactions :
        total += float(transaction["amount"])

    return total

# Read operation
@app.route("/")
def get_transactions() :
    total = get_transaction_total()

    return render_template("transactions.html", transactions=transactions, total=total)


# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction() :
    if request.method == "GET" :
        return render_template("form.html")
    
    elif request.method == "POST" :
        new_transaction = {
            "id":len(transactions)+1, 
            "date":request.form["date"],
            "amount":float(request.form["amount"])
            }
        transactions.append(new_transaction)
        return redirect(url_for("get_transactions"))


# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id) :
    if request.method == "GET" :
        for transaction in transactions :
            if transaction["id"] == transaction_id :
                return render_template("edit.html", transaction=transaction)
    elif request.method == "POST" :
        date = request.form["date"]
        amount = float(request.form["amount"])

        for transaction in transactions :
            if transaction["id"] == transaction_id :
                transaction["date"] = date
                transaction["amount"] = amount
                break
        
        return redirect(url_for("get_transactions"))
    




# Delete operation
@app.route("/delete/<int:transaction_id>", methods=["GET", "POST"])
def delete_transaction(transaction_id) :
    for transaction in transactions :
            if transaction["id"] == transaction_id :
                transactions.remove(transaction)
                break
    return redirect(url_for("get_transactions"))

 # search
@app.route("/search", methods=['GET', "POST"])
def search_transactions() :
    if request.method == 'POST' :
        found_transactions = []
        min_amount = float(request.form["min_amount"])
        max_amount = float(request.form["max_amount"])

        for transaction in transactions :
            if float(transaction["amount"]) >= min_amount and float(transaction["amount"]) <= max_amount :
                found_transactions.append(transaction)
        
        if len(found_transactions) > 0 :
            return render_template("transactions.html", transactions=found_transactions)
        
        else:
            return render_template("search.html", message="No Records Found - ")
        
    elif request.method == 'GET':
        return render_template("search.html")

# Total Balance
@app.route("/total", methods=["GET", "POST"])
def total_balance() :
    total = get_transaction_total()

    return render_template("transactions.html", transactions=transactions, total=total)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)