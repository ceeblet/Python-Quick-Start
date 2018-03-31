# Learn How to Make a Jinja Template and Basic Flask Web App
This is a basic Flask app that runs in debug mode, meaning you can make changes to the layout or the Python code generating the HTML page and refresh the page to see your changes. You don't have to rerun the script!

# Requirements
Python 3, Flask, knowledge of HTML

# Steps
1. Clone this repo.
2. `cd` to the directory where you cloned it and then into this one (`cd <where you cloned this>/learn_jinja_and_flask`)
3. Open up the terminal and run `python run_app.py`
4. Make changes as desired to the HTML (or to the variables you pass from Python) and simply refresh the pages to see your changes.

Note that you can pass variables to the template from Python. You will have to place those in the call to `render_template()` in the `run_app.py` file. This repo has `name = None` there as an example.

## Resources
* [Jinja Docs] (http://jinja.pocoo.org/docs/2.10/)
* [Flask Docs] (http://flask.pocoo.org/docs/0.12/quickstart/)
