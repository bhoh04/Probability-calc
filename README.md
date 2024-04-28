# Hat Experiment Probability Calculator

This is a Python program that estimates the probability of drawing certain balls randomly from a hat. It allows you to specify the number of balls in the hat, the expected combination of balls to draw, the number of balls drawn in each experiment, and the number of experiments to perform.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies (if not already installed) using pip:

```bash
pip install -r requirements.txt
```

4. Run the GUI application by executing the following command:

```bash
python gui.py
```

5. Enter the required inputs in the GUI and click "Calculate Probability" to get the result.

## Usage

- **Number of balls in the hat**: Enter the number of balls of each color in the hat. Separate each color and count with a space, and use the format `color:count` (e.g., `red:4 green:3 blue:2`).
- **Expected balls**: Enter the expected combination of balls to draw. Separate each color and count with a space, and use the format `color:count` (e.g., `red:2 green:1`).
- **Number of balls drawn**: Enter the number of balls to draw in each experiment.
- **Number of experiments**: Enter the number of experiments to perform.

## Example

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. You want to determine the probability of drawing at least 1 red ball and 2 green balls when drawing 4 balls from the hat. To do this, you can perform a certain number of experiments and estimate the probability accordingly.

For example:

- **Number of balls in the hat**: `blue:5 red:4 green:2`
- **Expected balls**: `red:1 green:2`
- **Number of balls drawn**: `4`
- **Number of experiments**: `1000`

The program will estimate the probability of drawing at least 1 red ball and 2 green balls in 4 draws from the hat based on the specified parameters.

## Author

Benjamin Hoh