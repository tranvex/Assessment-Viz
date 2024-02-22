import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_graph():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    # Create a new figure and a set of subplots
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(x, y)

    # Create a rounded rectangle patch
    round_rect = patches.FancyBboxPatch(
        (0, 0),
        1,
        1,
        boxstyle="round,pad=0.02",
        edgecolor="none",
        facecolor="none",
        transform=ax.transAxes,
    )
    round_rect.set_clip_on(False)

    # Add the rounded rectangle patch to the axes
    ax.add_patch(round_rect)

    # Set the axes' clip path to the rounded rectangle patch
    ax.set_clip_path(round_rect)

    return fig


def show_graph(fig):
    # Show the graph
    fig.show()
