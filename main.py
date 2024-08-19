import math, time, keyboard, random, sys

def drawScreen(x, y, pipe, gap, score, HI):

    print("--------------------------------------------------")

    for height in range(10):

        for width in range(52):

            if width == pipe and height != gap and height != gap + 1 and height != gap + 2:

                if width == x and height == y or width == x + 1 and height == y:
                    return True

                print("[]", end="")
                continue

            elif width == pipe + 1 and height != gap and height != gap + 1 and height != gap + 2:
                continue

            elif width == x and height == y:

                print("O", end="")
                continue

            elif width == x + 1 and height == y:

                print(">", end="")
                continue

            elif width == 0 or width == 51:
                
                print("|", end="")
                continue

            elif y < 0 or y > 9:

                return True

            print(" ", end="")

        print("")


    print("--------------------------------------------------\n\nScore:", score, "|", "High Score:", HI, "\n")
    
    return False

def loseScreen(HI):

    print("\n\n\n\n\n\n\n\n\n\n\nYOU LOSE!!!\n\n")

    answer = input("PLAY AGAIN??? (Y/N) ")

    if answer != "Y":
        
        file = open("file.txt", "w")
        file.write("High Score: " + str(HI) + "   \n\nFeel free to hack!\n\n Secret message, don't reveal! \n\n01001110 01100101 01110110 01100101 01110010 00100000 01100111 01101111 01101110 01101110 01100001 00100000 01100111 01101001 01110110 01100101 00100000 01111001 01101111 01110101 00100000 01110101 01110000 00001010 01001110 01100101 01110110 01100101 01110010 00100000 01100111 01101111 01101110 01101110 01100001 00100000 01101100 01100101 01110100 00100000 01111001 01101111 01110101 00100000 01100100 01101111 01110111 01101110 00001010 01001110 01100101 01110110 01100101 01110010 00100000 01100111 01101111 01101110 01101110 01100001 00100000 01110010 01110101 01101110 00100000 01100001 01110010 01101111 01110101 01101110 01100100 00100000 01100001 01101110 01100100 00100000 01100100 01100101 01110011 01100101 01110010 01110100 00100000 01111001 01101111 01110101 00001010 01001110 01100101 01110110 01100101 01110010 00100000 01100111 01101111 01101110 01101110 01100001 00100000 01101101 01100001 01101011 01100101 00100000 01111001 01101111 01110101 00100000 01100011 01110010 01111001 00001010 01001110 01100101 01110110 01100101 01110010 00100000 01100111 01101111 01101110 01101110 01100001 00100000 01110011 01100001 01111001 00100000 01100111 01101111 01101111 01100100 01100010 01111001 01100101 00001010 01001110 01100101 01110110 01100101 01110010 00100000 01100111 01101111 01101110 01101110 01100001 00100000 01110100 01100101 01101100 01101100 00100000 01100001 00100000 01101100 01101001 01100101 00100000 01100001 01101110 01100100 00100000 01101000 01110101 01110010 01110100 00100000 01111001 01101111 01110101 00100001 00001010 00001010 01010100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01110111 01101000 01100001 01110100 00100000 01111001 01101111 01110101 00100000 01100111 01100101 01110100 00001010 01010011 01110101 01100010 01110011 01100011 01110010 01101001 01100010 01100101")
        file.close()

        sys.exit()

while True:

    print("\n\n\n")

    birdX = 2
    birdY = 2
    velY = 0

    pipeX = 50
    pipeGapY = random.randint(1, 6)

    score = 0

    saveFile = open("file.txt", "r")

    highScore = int(saveFile.read()[12:16])

    while True:

        if keyboard.is_pressed("space"):
            velY = -1
            
        time.sleep(0.5)

        if keyboard.is_pressed("space"):
            velY = -1

        birdY += math.floor(velY)
        velY += 0.25
        pipeX -= 2

        if pipeX < 0:
            pipeX = 50
            pipeGapY = random.randint(1, 6)
            score += 1

        if score > highScore:
            highScore = score
                
        lose = drawScreen(birdX, birdY, pipeX, pipeGapY, score, highScore) 

        if lose:
            break

    loseScreen(highScore)

# Play area               
