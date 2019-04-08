from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Dashboard(MethodView):
    def get(self):
        """
        get data from model
        """
        model = gbmodel.get_model()
        teams = [dict(name=row[2]) for row in model.selectTeams()]
        students = [dict(name=row[3]) for row in model.selectStudents()]
        return render_template('dashboard.html', teams=teams, students=students)
