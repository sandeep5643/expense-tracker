from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Expense
from datetime import datetime
import os
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev-secret-key")

db.init_app(app)

@app.route("/")
def home():
    # show recent 5 expenses on home
    recent = Expense.query.order_by(Expense.date.desc()).limit(5).all()
    return render_template("index.html", recent=recent)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        date_str = request.form.get("date")
        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date_obj = datetime.today().date()

        category = request.form.get("category", "Other")
        amount = request.form.get("amount", "0").strip()
        note = request.form.get("note", "")

        try:
            amount_val = float(amount)
        except ValueError:
            flash("Amount should be a number", "danger")
            return redirect(url_for("add_expense"))

        exp = Expense(date=date_obj, category=category, amount=amount_val, note=note)
        db.session.add(exp)
        db.session.commit()
        flash("Expense added successfully!", "success")
        return redirect(url_for("view_expenses"))

    return render_template("add_expense.html")

@app.route("/expenses")
def view_expenses():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    total = sum(e.amount for e in expenses)
    return render_template("view_expenses.html", expenses=expenses, total=total)

@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    exp = Expense.query.get_or_404(expense_id)
    db.session.delete(exp)
    db.session.commit()
    flash("Expense deleted", "info")
    return redirect(url_for("view_expenses"))

@app.route("/stats")
def stats():
    # category-wise sum
    category_data = db.session.query(
        Expense.category,
        func.sum(Expense.amount).label("total")
    ).group_by(Expense.category).all()

    # monthly totals (YYYY-MM)
    monthly_data = db.session.query(
        func.strftime("%Y-%m", Expense.date).label("month"),
        func.sum(Expense.amount).label("total")
    ).group_by("month").order_by("month").all()

    return render_template("stats.html", category_data=category_data, monthly_data=monthly_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
