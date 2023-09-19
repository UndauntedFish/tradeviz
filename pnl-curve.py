import matplotlib.pyplot as plt
import numpy as np


def generate_curve_from_rr_wr(win_loss_ratio: float, win_rate: float, num_trades_to_simulate: int = 1000):
    """
    Generate an equity curve based on win:loss ratio and win rate.

    Parameters:
        win_loss_ratio (float): The win:loss ratio for each trade.
        win_rate (float): The win rate as a decimal (e.g., 0.6 for a 60% win rate).
        starting_capital (float): Initial capital (default is $10,000.00).
        num_data_points (int): Number of data points for the equity curve (default is 100).

    Returns:
        None, plots the equity curve.

    Explanation:
        This method generates a hypothetical equity curve based on a specified reward-risk ratio.
        The equity curve is created by simulating trading returns where each data point represents either a
        positive return (reward) or a negative return (risk) based on the given reward-risk ratio.

        The generated equity curve is then plotted to visualize the performance of a trading strategy with
        the specified reward-risk profile.

    Example Usage:
        generate_curve_from_rr_ratio(2.0, 0.4)  # Generates an equity curve with a reward-risk ratio of 2:1 and a winrate of 40%
    """
    # Initialize an array to store returns
    returns = []

    # Generate returns for each trade based on win rate and reward-to-risk ratio
    for _ in range(num_trades_to_simulate):
        if np.random.rand() < win_rate:
            returns.append(win_loss_ratio)
        else:
            returns.append(-1)

    # Calculate equity curve by cumulatively multiplying each trading return
    equity_curve_uncompounded = np.cumsum(returns)

    # Calculate expected value per trade (EV) to display in the plot title. Round it to the nearest thousandth (3 decimal places).
    ev = round((win_rate * win_loss_ratio) - (1-win_rate), 3)

    # Plot the equity curve
    plt.figure(figsize=(10, 6))
    plt.plot(equity_curve_uncompounded, label = "Accumulated R", color = "blue")
    plt.xlabel("Number of Trades Taken")
    plt.ylabel("Accumulated R")
    plt.title(f"Accumulated R vs Number of Trades Taken (W:L = {win_loss_ratio}, WR = {win_rate * 100}%, EV = {ev}R)")
    plt.grid(True)

    # Show the plot
    plt.show()