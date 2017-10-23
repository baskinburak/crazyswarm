#!/usr/bin/env python

from pycrazyswarm import *
import numpy as np

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs


    allcfs.takeoff(targetHeight=1.0, duration=2.0)
    timeHelper.sleep(2.0)


    print("press button to go into boids mode")
    swarm.input.waitUntilButtonPressed()

    allcfs.boids()

    cf = allcfs.crazyfliesById[5]
    cf.boids(allcfs.BOIDS_LEADER, [1.0,1.0,1.0])

    print("press button to change dest")
    swarm.input.waitUntilButtonPressed()

    
    cf.boids(allcfs.BOIDS_LEADER, [-1.0,-1.0,1.0])
    
    print("press button to land")
    swarm.input.waitUntilButtonPressed()

#    for cf in allcfs.crazyflies:
#        pos = np.array(cf.initialPosition) + np.array([0, 0, 1])
#        cf.hover(pos, 0, 4.0)


#    timeHelper.sleep(4.5)


#    print("hover ended")


    allcfs.land(0.02, 3)
    timeHelper.sleep(3.0)
