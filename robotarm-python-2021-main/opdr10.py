from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
r=9
for a in range(5):
    robotArm.grab()
    for i in range(r):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(r):
        robotArm.moveLeft()
    robotArm.moveRight()
    r-=2
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()