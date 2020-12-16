import numpy as np
import random
import vispy.plot as vp
import vispy.io as io
import vispy.visuals as vs

def main():

    nitems = int(input("Enter number of items: "))
    
    dataout = np.random.randn(nitems,2)

    #start_time = datetime.now()
    #process = subprocess.Popen(FG_GNUPLOT_DIR,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #print("Process started: %s" % process.pid)
    #output = process.communicate(bytes("\n".join(command) + "\n","utf-8") + dataout.tostring())
    #print("Process finished: %s (code: %s)" % (process.pid, process.returncode))
    #end_time = datetime.now() - start_time
    #end_time = end_time.total_seconds()
    
    # Using vispy.plot
    # Plot data
    fig = vp.Fig(show=False)
    fig[0,0].plot(dataout)
    
    # render to generate image object
    img= fig.render()
    
    # Export as png
    img_out = io.write_png("plot.png",img)

    # Using vispy example
    
    n = 100000
    data = np.random.randn(n, 2)
    color = (0.8, 0.25, 0.)

    fig = vp.Fig(show=False)
    fig[0:4, 0:4].plot(data, width=0, face_color=color + (0.05,), edge_color=None,
                   marker_size=100.)

    img = fig.render()
    io.write_png("otherplot.png", img)
main()
