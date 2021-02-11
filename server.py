from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world" #this is the response 


@app.route("/allfood") #localhost:5000/allfood
def showAllFoodItems():
    return render_template("foodlist.html")

@app.route("/success")
def success():
    return "You are in the success page for when you order some food"

@app.route("/team/<teamname>") #routing with parameters 
def showSpecificTeam(teamname):
    teamlist = ["lakers", "wizards", "warriors"]
    if teamname in teamlist:
        return f"Placeholder to later show information about one team: {teamname}"
    else:
        return "sorry this team does not exist"


@app.route("/showPlayer/<int:num>/<celebrity>")
def showcelebrity(num, celebrity):
    nombre = "El chapo"
    return render_template("showCelebrity.html", x = nombre, celebrity=celebrity, num = num)


@app.route("/crypto/bitcoins")
def showcrypto():
    return render_template("crypto.html")

@app.route("/crypto/bitcoins/<int:numcoins>")
def showNumCrypto(numcoins):
    return render_template("crypto2.html", numcoins=numcoins)



@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "THESE ARE NOT THE DROIDS YOU'RE LOOKING FOR"





if __name__ == "__main__":
    app.run(debug=True)
