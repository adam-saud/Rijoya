from flask import Flask, render_template , json , request , redirect , url_for , session , os , jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# مسار للإدمن
@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# تحديد مكان ملف JSON
ADMIN_FILE = "admins.json"

# دالة مساعدة لتحميل البيانات
def load_admins():
    if os.path.exists(ADMIN_FILE):
        with open(ADMIN_FILE, "r") as f:
            return json.load(f)
    return []

# دالة مساعدة لحفظ البيانات
def save_admins(admins):
    with open(ADMIN_FILE, "w") as f:
        json.dump(admins, f, indent=4)

@app.route("/admin/signup", methods=["POST"])
def admin_signup():
    new_user = request.form.get("new_admin_user")
    new_password = request.form.get("new_admin_password")

    admins = load_admins()

    # إضافة الأدمن الجديد
    admins.append({
        "username": new_user,
        "password": new_password  # ⚠️ للتجربة فقط، الأفضل تستخدم hashing
    })

    save_admins(admins)

    return jsonify({"message": "Admin added successfully!", "admins": admins})


if __name__ == '__main__':
        app.run(debug=True)
