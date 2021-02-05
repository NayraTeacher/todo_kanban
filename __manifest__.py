# -*- encoding: utf-8 -*-
{
    'name': 'To-do App Kanban',
    'version': '1.0',
    'author': 'EEP - Profesor',
    'description': """ Tablero Kanban para tareas To-Do.""",
    'depends': ['todo_user','board'],
    'data': ['views/todo_kanban_views.xml',
             'views/todo_board_views.xml',
             'views/todo_hours_report.xml',
             'reports.xml'],
}
