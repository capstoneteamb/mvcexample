from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class AddStudent(MethodView):
    def get(self):
        return render_template('addStudent.html')

    def post(self):
        """
        Accepts POST requests and gets the data from the form
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insertStudent(request.form['studentName'], request.form['studentID'], 
        request.form['sessionID'], request.form['teamID'])
        return redirect(url_for('addStudent'))


class AddTeam(MethodView):
    def get(self):
        return render_template('addTeam.html')

    def post(self):
        """
        Accepts POST requests and gets the data from the form
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insertTeam(request.form['teamID'], 
        request.form['sessionID'],request.form['teamName'])
        return redirect(url_for('addTeam'))
