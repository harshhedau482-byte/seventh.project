# NumPy Data Analytics

A menu-driven Python project for creating, manipulating, and analyzing NumPy arrays. It demonstrates object-oriented programming concepts such as encapsulation, instance methods, static methods, and class methods.

## Features

- **Array creation:** Create 1D, 2D, and 3D arrays.
- **Indexing and slicing:** Access individual elements and extract parts of arrays.
- **Mathematical operations:** Perform addition, subtraction, element-wise multiplication, division, and matrix multiplication.
- **Combine and split:** Join arrays and split an array into multiple parts.
- **Search, sort, and filter:** Find values, sort elements in ascending or descending order, and filter values greater than a threshold.
- **Statistics:** Calculate sum, mean, median, standard deviation, variance, minimum, maximum, and percentiles.
- **Object-oriented design:** Uses a `DataAnalytics` class with a private array attribute, getter/setter methods, a static method, and a class method.

## Requirements

- Python 3.8 or later
- NumPy

## Installation

1. Make sure Python is installed.
2. Install NumPy:

   ```bash
   pip install numpy
   ```

3. Save the program in a file, for example `main.py`.

## Run the Program

Open a terminal in the project directory and run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## How to Use

When the program starts, select an option from the main menu:

| Option | Description |
| --- | --- |
| 1 | Create a NumPy array (1D, 2D, or 3D), then optionally use indexing or slicing |
| 2 | Perform mathematical operations on the current array |
| 3 | Combine the current array with another array or split it into parts |
| 4 | Search, sort, or filter array values |
| 5 | Display aggregate statistics |
| 6 | Exit the program |

Follow the prompts and enter the requested values. For array creation, provide the exact number of elements requested so they can be reshaped into the selected dimensions.

## Example

For a 1D array, select option `1`, choose `1D Array`, enter `5` elements, then enter:

```text
10 20 30 40 50
```

The resulting array is:

```text
[10. 20. 30. 40. 50.]
```

Choose option `5` to display statistics such as the sum, mean, median, standard deviation, variance, minimum, and maximum.

## Project Structure

```text
numpy-data-analytics/
├── main.py
└── README.md
```

## Notes and Limitations

- Array indexing is **zero-based**. For example, index `0` refers to the first element.
- NumPy array operations may require compatible shapes.
- The current mathematical-operations menu asks for a second array with the same shape as the first array. Matrix multiplication only works when the matrix dimensions are compatible; for a more general matrix-multiplication workflow, the second-array input should be updated to accept a different shape.
- Combining arrays with `axis=0` requires compatible dimensions along the other axes. In particular, combining 2D arrays requires matching column counts.
- Division by zero can produce NumPy warnings or infinite values.
- The current menu calculates statistics but does not provide a menu option for the `calculate_percentile()` method.
- The `create_array(dim, shape, elements)` method currently uses `shape` to reshape the data; the `dim` argument is not used for validation.

## Concepts Demonstrated

- Classes and objects
- Constructor (`__init__`)
- Encapsulation using a private attribute (`__array`)
- Getter and setter methods
- Static methods (`@staticmethod`)
- Class methods (`@classmethod`)
- NumPy arrays, indexing, slicing, and reshaping
- Array arithmetic and matrix multiplication
- Searching, sorting, filtering, and statistical analysis

## Author

Add your name here.

## License

No license has been specified. Add a license file if you intend to distribute this project publicly.

