## Mandelbrot Set Visualization

This project generates and visualizes the **Mandelbrot set** using Python and `matplotlib`. The Mandelbrot set is a famous fractal structure defined in the complex plane.

### Description

The Mandelbrot set is created by iterating the function:

$$
z_{n+1} = z_n^2 + c
$$

starting from $z_0 = 0$, where $c$ is a complex number. A point $c$ belongs to the Mandelbrot set if the magnitude of $z$ does not tend toward infinity after many iterations.

This script:

* Generates a 2D grid of complex numbers,
* Iteratively checks whether each number belongs to the Mandelbrot set,
* Visualizes the results with a color map using `matplotlib`.

### How It Works

* Resolution: 2000x2000 pixels
* Iteration limit: 150
* Points that "escape" early are colored differently from those that remain in the set
* Colormap used: `hot`

### Files

* `mandelbrot.py`: Main Python script to generate and display the fractal.

###  How to Run

Make sure you have Python and the required packages installed:

```bash
pip install matplotlib numpy
```

Then run the script:

```bash
python mandelbrot.py
```

A window will open displaying the Mandelbrot set.

### Example Output

The plot shows the Mandelbrot set in the complex plane, with colors representing the number of iterations before escape.

### Parameters You Can Change

* `width`, `height`: Image resolution
* `max_iter`: Maximum number of iterations per point
* `xmin`, `xmax`, `ymin`, `ymax`: Zoom level
* `cmap`: Try different color maps like `'viridis'`, `'plasma'`, `'inferno'`

### 📚 References

* [Wikipedia: Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set)
* [Fractals in Python](https://realpython.com/mandelbrot-set-python/)
