# SimpleV: Matrix to HTML Image Generator

`SimpleV` is a Python class that generates an HTML file representing a visual image based on a given matrix. Each element in the matrix corresponds to a colored cell in the output HTML, making it easy to visualize data in a grid format.

## Features

- Generates a customizable HTML file with a visual representation of a matrix.
- Allows specification of cell size and color mapping for different values in the matrix.
- Saves the generated HTML file locally for easy viewing in a web browser.

## Requirements

- Python 3.x

## Installation

You can use this class directly in your Python scripts. No additional installation is required.

## Usage

1. **Import the Class**: First, ensure you have the `SimpleV` class defined in your script.

2. **Prepare Your Data**:
   - Create a matrix (list of lists) where each inner list represents a row.
   - Define a color map (dictionary) that maps each unique value in the matrix to a specific color.

3. **Initialize the Class**:
   - Create an instance of the `SimpleV` class, passing in your matrix, cell size, color map, and an optional output filename.

4. **Generate and Save HTML**:
   - Call the `save_to_file()` method on the instance to generate the HTML file.

### Example

```python
# Define a sample matrix
matrix = [
    [0, 1, 2],
    [1, 2, 0],
    [2, 0, 1]
]

# Define a color map
color_map = {
    0: "red",
    1: "green",
    2: "blue"
}

# Set cell size (in pixels)
cell_size = 50

# Create an instance of SimpleV
image_generator = SimpleV(matrix, cell_size, color_map)

# Generate the HTML file
image_generator.save_to_file()
```

## Output

After running the above example, you will find a file named `generated_image.html` in your working directory. Open this file in a web browser to view the generated image.

## Customization

- **Cell Size**: Adjust the `cell_size` parameter to change the dimensions of each cell in the generated grid.
- **Color Mapping**: Modify the `color_map` dictionary to customize the colors associated with each value in your matrix.
- **Output Filename**: You can change the default output filename by passing a different name when initializing the `SimpleV` class.

## License

This project is open-source and available under the MIT License. Feel free to use and modify it as needed.