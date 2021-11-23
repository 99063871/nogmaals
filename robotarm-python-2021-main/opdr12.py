from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
blocks = 9
for i in range(9):
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == "red":
        for a in range(blocks):
            robotArm.moveRight()
        robotArm.drop()
        blocks-=1
        for a in range(blocks):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        blocks-=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()