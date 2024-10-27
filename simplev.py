class SimpleV:
    def __init__(self, matrix, cell_size, color_map, output_filename="generated_image.html"):
        self.matrix = matrix
        self.cell_size = cell_size
        self.color_map = color_map  
        self.output_filename = output_filename  

    def generate_html(self):
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Generated Image</title>
<style>
  .container {{
    display: flex;
    flex-direction: column;
  }}
  .row {{
    display: flex;
  }}
  .cell {{
    width: {self.cell_size}px;
    height: {self.cell_size}px;
  }}
</style>
</head>
<body>
<div class="container">
"""
        for row in self.matrix:
            html_content += '  <div class="row">\n'
            for value in row:
                color = self.color_map.get(value, "transparent")
                html_content += f'    <div class="cell" style="background-color: {color};"></div>\n'
            html_content += '  </div>\n'

        html_content += """</div>
</body>
</html>
"""

        return html_content

    def save_to_file(self):
        html_content = self.generate_html()
        with open(self.output_filename, "w") as file:
            file.write(html_content)
        print(f"HTML file generated successfully as '{self.output_filename}'.")


