from bokeh.plotting import figure, output_file, save
from bokeh.models import Slider, CustomJS, ColumnDataSource
from bokeh.layouts import column
import numpy as np

# Function to generate logistic function data
def generate_logistic_function(x, gain, bias, offset):
    return 1 / (1 + np.exp(-gain * (x - bias) + offset))

# Initial parameters
x = np.linspace(-10, 10, 500)
initial_gain = 1.0
initial_bias = 0.0
initial_offset = 0.0
y = generate_logistic_function(x, initial_gain, initial_bias, initial_offset)

# Create a ColumnDataSource
source = ColumnDataSource(data={"x": x, "y": y})

# Create the Bokeh figure
plot = figure(
    title=f"Logistic Function",
    x_axis_label="x",
    y_axis_label="y",
    width=800,
    height=400,
)

# Add the initial line to the plot
plot.line("x", "y", source=source, line_width=2, line_color="blue")

# Define sliders for gain, bias, and offset
gain_slider = Slider(start=0.1, end=5.0, value=initial_gain, step=0.1, title="Gain")
bias_slider = Slider(start=-5.0, end=5.0, value=initial_bias, step=0.1, title="Bias")
offset_slider = Slider(start=-1.0, end=1.0, value=initial_offset, step=0.1, title="Offset")

# JavaScript callback to update the plot
callback = CustomJS(
    args=dict(
        source=source,
        gain_slider=gain_slider,
        bias_slider=bias_slider,
        offset_slider=offset_slider,
    ),
    code="""
        const data = source.data;
        const x = data['x'];
        const gain = gain_slider.value;
        const bias = bias_slider.value;
        const offset = offset_slider.value;

        // Update y values
        for (let i = 0; i < x.length; i++) {
            data['y'][i] = 1 / (1 + Math.exp(-gain * (x[i] - bias) + offset));
        }

        // Update title
        source.change.emit();
    """,
)

# Link sliders to the callback
gain_slider.js_on_change("value", callback)
bias_slider.js_on_change("value", callback)
offset_slider.js_on_change("value", callback)

# Arrange sliders and plot in a column layout
layout = column(plot, gain_slider, bias_slider, offset_slider)

# Save to HTML
output_file("interactive_logistic.html")
save(layout)

print("HTML file created: interactive_logistic_function_bokeh.html")
