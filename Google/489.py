# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, [], 0, 0)



    def dfs(self, robot, record, i, j):
        if (i , j) in record:
            return
        record.append((i, j))
        robot.clean()

        # up
        if robot.move():
            self.dfs(robot, record, i - 1, j)
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
        else:
            robot.turnLeft()
            robot.turnLeft()

        # down
        if robot.move():
            robot.turnLeft()
            robot.turnLeft()
            self.dfs(robot, record, i + 1, j)
            robot.move()
            robot.turnLeft()
        else:
            robot.turnLeft()
            robot.turnLeft()
            robot.turnLeft()

        # left
        if robot.move():
            robot.turnRight()
            self.dfs(robot, record, i, j - 1)
            robot.turnRight()
            robot.move()
        else:
            robot.turnRight()
            robot.turnRight()

        # right
        if robot.move():
            robot.turnLeft()
            self.dfs(robot, record, i, j + 1)
            robot.turnLeft()
            robot.move()
            robot.turnRight()
        else:
            robot.turnLeft()


