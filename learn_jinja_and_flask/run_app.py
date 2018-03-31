from flask import Flask, render_template, url_for

app = Flask(__name__)

# this defines an endpoint where your app is available.
# Currently the app is only reachable at localhost:5000/ or localhost:5000
@app.route('/')
def page(): # the name of this function can be used if you use redirects (you can read about this in the Flask documentation)
	return render_template('sample_template.html', name = None) # change this to your name to see it show up

if __name__ == '__main__':
	app.run(debug=True)
	# visit localhost:5000 in your browser to see your page after starting the script.
	# edit as you wish
