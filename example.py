from simplev import SimpleV

matrix = [
    [1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 5, 1, 1, 1, 1],
    [1, 1, 2, 3, 3, 3, 5, 1, 1, 1, 1],
    [1, 1, 2, 3, 3, 3, 5, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 5, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1],
]

color_map = {
    1: "yellow",  
    2: "black",   
    3: "white",
    5: "green",   
}


generator = SimpleV(matrix, cell_size=50, color_map=color_map, output_filename="output.html")

generator.save_to_file()
