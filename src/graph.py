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





'''
-> Should probably add a way to interact with the files being read in.
-> Of course when graphing you may run into the error: "you're trying to graph 
-> a non numerical value (something along those liens)" possibly it complaining about
-> converting a string to int.

-> how to read a file -> example = pd.read("filename or filepath")
-> is may depend on how miklos is reading the files. It is possible that you just call his file attribute <-

-> To handle the error, maybe specify the columns you want to graph like
-> df ['columnName'] = pd.scatter(df['columnName'], label = 'whatever you want to call it')
-> keep in mind there are a number of different graphs, scatter, plot, bar. 
-> so you can do pd.plot as well. 

-> .show() is how we call our graph to be shown. without it nothing would appear.
-> .grid() will add grid lines to the graph.
-> marker = 'o' will add dots for each point if we do a line graph. 
'''