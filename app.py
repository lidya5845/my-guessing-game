
from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "my-game-secret-key"


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    result = ""
    player_name = ""

    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 10)

    if request.method == "POST":
        player_name = request.form.get("player_name", "").strip()
        guess = request.form.get("guess", type=int)

        if not player_name:
            message = "اكتبي اسمك أولًا 🧡"

        elif guess is None or not 1 <= guess <= 10:
            message = f"يا {player_name}، اكتبي رقمًا من 1 إلى 10! 👀"

        elif guess < session["secret_number"]:
            message = f"الرقم السري أكبر يا {player_name}! 👀"
            result = "sad"

        elif guess > session["secret_number"]:
            message = f"الرقم السري أصغر يا {player_name}! 🤏"
            result = "sad"

        else:
            message = f"صححح يا {player_name}! خمنتي الرقم 🎉🏆"
            result = "happy"
            session["secret_number"] = random.randint(1, 10)

    return render_template(
        "index.html",
        message=message,
        result=result,
        player_name=player_name
    )


if __name__ == "__main__":
    app.run(debug=True)
