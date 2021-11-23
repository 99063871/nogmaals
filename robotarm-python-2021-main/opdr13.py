from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
blocks = 1
robotArm.grab()
robotArm.scan()
while robotArm.scan() != "":
    for i in range(blocks):
        robotArm.moveRight()
    robotArm.drop()
    for a in range(blocks):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.scan()
    blocks+=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()