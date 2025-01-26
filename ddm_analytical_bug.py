from scipy.stats import pearson3
import psyneulink as pnl
import numpy as np
import matplotlib.pyplot as plt


# In the following code, rt_mean_correct and rt_mean_incorrect should differ, but they don't

num_trials = 1

# Instate the DDM mechanism
ddm_integrator = pnl.DDM(function=pnl.DriftDiffusionAnalytical(
    noise=.25,
    starting_value=0.0,
    non_decision_time=0.0,
    drift_rate=.05,
    threshold=1.0),
    output_ports=[pnl.PROBABILITY_UPPER_THRESHOLD, pnl.PROBABILITY_LOWER_THRESHOLD, pnl.RT_CORRECT_MEAN, pnl.RT_CORRECT_VARIANCE, pnl.RT_CORRECT_SKEW, pnl.RT_INCORRECT_MEAN, pnl.RT_INCORRECT_VARIANCE, pnl.RT_INCORRECT_SKEW]
)

# Create a compositions with only the integrator
DDM = pnl.Composition(name='DDM')
DDM.add_node(node=ddm_integrator)

# Run it
DDM.run(inputs={ddm_integrator: .5}, num_trials=num_trials, context='execid')

# Extract the data (here we access the values directly)
probability_correct = ddm_integrator.output_ports[pnl.PROBABILITY_UPPER_THRESHOLD].value[0]
probability_incorrect = ddm_integrator.output_ports[pnl.PROBABILITY_LOWER_THRESHOLD].value[0]

rt_correct_mean = ddm_integrator.output_ports[pnl.RT_CORRECT_MEAN].value[0]
rt_correct_variance = ddm_integrator.output_ports[pnl.RT_CORRECT_VARIANCE].value[0]
rt_correct_skew = ddm_integrator.output_ports[pnl.RT_CORRECT_SKEW].value[0]
rt_correct_std = np.sqrt(rt_correct_variance)

rt_incorrect_mean = ddm_integrator.output_ports[pnl.RT_INCORRECT_MEAN].value[0]
rt_incorrect_variance = ddm_integrator.output_ports[pnl.RT_INCORRECT_VARIANCE].value[0]
rt_incorrect_skew = ddm_integrator.output_ports[pnl.RT_INCORRECT_SKEW].value[0]
rt_incorrect_std = np.sqrt(rt_incorrect_variance)

# Generate the Pearson Type III distributions
x_correct = np.linspace(rt_correct_mean - 4 * rt_correct_std, rt_correct_mean + 4 * rt_correct_std, 1000)
pdf_correct = pearson3.pdf(x_correct, rt_correct_skew, loc=rt_correct_mean, scale=rt_correct_std) * probability_correct

x_incorrect = np.linspace(rt_incorrect_mean - 4 * rt_incorrect_std, rt_incorrect_mean + 4 * rt_incorrect_std, 1000)
pdf_incorrect = pearson3.pdf(x_incorrect, rt_incorrect_skew, loc=rt_incorrect_mean, scale=rt_incorrect_std) * probability_incorrect

# Plot the distribution
plt.plot(x_correct, pdf_correct, label=f'Correct', color='blue')
plt.plot(x_incorrect, pdf_incorrect, label=f'Incorrect', color='orange')
plt.title('Analytical RT distributions')
plt.xlabel('RT')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.show()


#### This is replicated here ####
# The first and third entry should be different but they aren't

fct = pnl.DriftDiffusionAnalytical(
    noise=.25,
    starting_value=0.0,
    non_decision_time=0.0,
    drift_rate=-.05,
    threshold=1.0)

res = fct.execute(1)


#### Here is the equations (I think they are wrong) ####

noise = .25
starting_value = 0.0
non_decision_time = 0.0
drift_rate = .05
threshold = 1.0

X = drift_rate * starting_value / noise ** 2
Z = drift_rate * threshold / noise ** 2

X = max(-100, min(100, X))

Z = max(-100, min(100, Z))

print(X, Z)


def coth(x):
    return np.cosh(x) / np.sinh(x)


def csch(x):
    return 1 / np.sinh(x)


plus = noise ** 2 / (drift_rate ** 2) * (2 * Z * coth(2 * Z) - (X + Z) * coth(X + Z))  # This is the same as minus if X == 0 (meaning starting_value == 0)
minus = noise ** 2 / (drift_rate ** 2) * (2 * Z * coth(2 * Z) - (-X + Z) * coth(-X + Z))



print(plus, minus)


