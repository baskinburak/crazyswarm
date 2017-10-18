#!/usr/bin/env python

from pycrazyswarm import *

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs


    allcfs.takeoff(targetHeight=2.0, duration=2.0)
    timeHelper.sleep(2.0)

    allcfs.boids()


    allcfs.crazyflies[0].boids(allcfs.BOIDS_LEADER, [0.0, 0.0, 0.0])

    swarm.input.waitUntilButtonPressed()


    allcfs.crazyflies[0].boids(allcfs.BOIDS_LEADER, [-10.0, -10.0, -10.0])

    swarm.input.waitUntilButtonPressed()


    allcfs.crazyflies[0].boids(allcfs.BOIDS_LEADER, [30.0, 30.0, 30.0])
    allcfs.crazyflies[1].boids(allcfs.BOIDS_LEADER, [0.0, 0.0, 0.0])

    swarm.input.waitUntilButtonPressed()

    allcfs.crazyflies[1].boids(allcfs.BOIDS_FOLLOWER, [0.0, 0.0, 0.0])

    swarm.input.waitUntilButtonPressed()
