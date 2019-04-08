from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class RemoveStudent(MethodView):
    def get(self):
        return render_template('removeStudent.html')

    def post(self):
        """
        Accepts POST requests and gets the data from the form
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.removeStudent(request.form['studentID'], 
        request.form['sessionID'])
        return redirect(url_for('removeStudent'))


class RemoveTeam(MethodView):
    def get(self):
        return render_template('removeTeam.html')

    def post(self):
        """
        Accepts POST requests and gets the data from the form
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.removeTeam(request.form['teamID'], 
        request.form['sessionID'])
        return redirect(url_for('removeTeam'))

