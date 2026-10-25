class Task:
    def __init__(self, title):
        self.title = title
        self.done = False


tasks = [Task("Купить тетрадь"), Task("Сделать лабу 3")]


@app.route("/")
def index():
    html = "<h1>Список дел</h1><ul>"
    for task in tasks:
        html += f"<li>{task.title}</li>"
    html += "</ul>"
    return html
