import os

# Build all python classes with diagrams dynamically

class DiagramBuilder:
    def __init__(self, filename, diagram_code):
        self.filename = filename
        self.diagram_code = diagram_code

    def generate_diagram(self):       
        exec(self.diagram_code)


if __name__ == "__main__":
    directory_path = "."

    for root, dirs, files in os.walk(directory_path):        
        for file_name in files:
            if file_name.endswith(".py") and not file_name.__contains__("DiagramBuilder"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r") as file:
                    diagram_code = file.read()
                    diagram_builder = DiagramBuilder(file_name[:-3], diagram_code)
                    diagram_builder.generate_diagram()
                    
